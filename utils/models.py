from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    func,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy_serializer import SerializerMixin


class Base(object):
    """Base class for all SQLAlchemy models"""

    created_at = Column("created_at", Date, default=func.now())
    updated_at = Column("updated_at", Date, default=func.now(), onupdate=func.now())


Base = declarative_base(cls=Base)


class Categories(Base, SerializerMixin):
    """
    Class representing Categories data.
    """

    __tablename__ = "catagories"

    category_id = Column("catagory_id", Integer, primary_key=True)
    name = Column("name", String)
    image_location = Column("image_location", String)
        
    def __repr__(self):
        return f"Category({self.category_id},{self.name},{self.image_location})"

class Items(Base, SerializerMixin):
    """
    Class representing Items data.
    """

    __tablename__ = "items"

    item_id = Column("item_id", Integer, primary_key=True)
    item_name = Column("item_name", String)
    item_code = Column("item_code", String)
    description = Column("description", String)
    image_location = Column("image_location", String)
    price = Column("price", Integer)
    dimensions = Column("dimensions", String)
    material = Column("material", String)
    colour = Column("colour", String)
    in_stock = Column("in_stock", Boolean)
    category_id = Column("catagory_id", Integer, ForeignKey(Categories.category_id))
    catagory = relationship(Categories, lazy="joined")

        
    def __repr__(self):
        return f"Item({self.item_id},{self.item_name},{self.image_location},{self.description},{self.price},{self.dimensions},{self.material},{self.colour},{self.in_stock},{self.item_code})"



