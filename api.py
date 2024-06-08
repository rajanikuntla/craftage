from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

import firebase_admin
from firebase_admin import credentials

from utils.twilio_utils import send_otp, verify_otp

from utils.login_utility import get_user_token

from utils.api_utils import (
get_categories, get_items, get_item, insert_category,
insert_item
)
from utils.api_models import Category, Item, Request, PhoneNumberRequest

cred = credentials.Certificate("config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/list")
def get_all_categories():
    categories = get_categories()
    if categories == None:
        return JSONResponse(content={'error': 'No categories found'}, status_code = 400) 
    categories_json = [category.to_dict() for category in categories]
    return JSONResponse(content={ 'result': categories_json}, status_code=200)
    

@app.get("/items/{category_id}")
def get_items_for_category(category_id):
    items = get_items(category_id)
    if items == None:
        return JSONResponse(content={'error': 'No items found for category'}, status_code = 400)   
    items_json = [item.to_dict() for item in items]     
    return JSONResponse(content={'result': items_json}, status_code = 200)

@app.get("/item/{item_id}")
def fetch_item(item_id):
    item = get_item(item_id)
    if item == None:
        return JSONResponse(content={'error': 'No item found'}, status_code = 400)        
    return JSONResponse(content={'result': item.to_dict()}, status_code = 200)

@app.post("/catagory")
def add_category(category: Category):
    inserted = insert_category(category)
    if not inserted:
        return JSONResponse(content={'error': 'Category cannot be saved'}, status_code = 400)        
    return JSONResponse(content={'Category saved successfully'}, status_code = 200)

@app.post("/item")
def add_item(item: Item):
    inserted = insert_item(item)
    if not inserted:
        return JSONResponse(content={'error': 'Item cannot be saved'}, status_code = 400)        
    return JSONResponse(content={'Item saved successfully'}, status_code = 200)

@app.post("/send-otp")
def send_verification_code(request: PhoneNumberRequest):
    if request.phone_number:
        status = send_otp(request.phone_number)
        if not status:
            return JSONResponse(content={'error': 'Valid Phone number is required'}, status_code = 400)        
        return JSONResponse(content={'status': status}, status_code = 200)
    return JSONResponse(content={'error': 'Phone number is required'}, status_code = 400)

@app.post("/login")
def verify_phone_number(request: Request):
    phone_number = request.phone_number
    otp = request.otp
    if phone_number and otp:
        is_verified = verify_otp(phone_number, otp)
        if is_verified:
            custom_token = get_user_token(phone_number)
            return JSONResponse(content={'result': custom_token.decode()}, status_code = 200)
        return JSONResponse(content={'error': 'Invalid OTP'}, status_code = 400) 
    return JSONResponse(content={'error': 'Phone number and OTP are required'}, status_code = 400)




