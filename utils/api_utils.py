
from utils.dbutils import db_engine
from sqlalchemy.orm import Session
from sqlalchemy import exc

from utils.models import Categories, Items

def get_categories():
    try:

        with Session(db_engine) as session:
            categories = session.query(Categories).all()
            return categories
        
    except Exception as e:
        print(e)
        return None

def get_items(category_id):
    try:
        with Session(db_engine) as session:
            items = session.query(Items).filter(Items.category_id == category_id).all()
            return items
        
    except Exception as e:
        print(e)
        return None

def get_item(item_id):
    try:
        with Session(db_engine) as session:
            item = session.query(Items).filter(Items.item_id == item_id).first()
            return item
        
    except Exception as e:
        print(e)
        return None
        

def insert_category(category):
    try:
        new_category = Categories()
        new_category.name = category.name
        # new_category.image_location = category.image_location
        with Session(db_engine) as session:
            session.add(new_category)
            session.commit() 
        return True

    except Exception as e:
        print(e)
        return False
    

def insert_item(item):
    try:
        new_item = Items()
        new_item.item_name = item.item_name
        new_item.item_code = item.item_code
        new_item.description = item.description
        new_item.price = item.price
        new_item.dimensions = item.dimensions
        new_item.material = item.material
        new_item.colour = item.colour
        new_item.in_stock = item.in_stock
        new_item.category_id = item.category_id
        with Session(db_engine) as session:
            session.add(new_item)
            session.commit() 
        return True

    except Exception as e:
        print(e)
        return False
