from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

association_table = Table('operations', Base.metadata,
                          Column('user_id', Integer, ForeignKey('users.id')),
                          Column('product_id', Integer, ForeignKey('products.id')),
                          Column('date_added', DateTime(timezone=True), server_default=func.now()))


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    avatar = Column(String)
    date_added = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())
    balance = Column(Float)


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    img = Column(String)
    cost = Column(Float)
    date_added = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())
    operations = relationship("Users", backref="operations", cascade="all,delete,save-update",
                              secondary=association_table)
