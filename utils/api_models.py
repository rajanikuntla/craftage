from pydantic import BaseModel


class Category(BaseModel):
    name: str

class Item(BaseModel):
    item_name: str
    item_code: str
    description: str
    price: int
    dimensions: str
    material: str
    colour: str
    in_stock: bool
    category_id: int

class Location(BaseModel):
    image_location: str


class Request(BaseModel):
    phone_number:str
    otp: str
