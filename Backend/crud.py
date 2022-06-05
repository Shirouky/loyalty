from sqlalchemy import create_engine, insert
from sqlalchemy.orm.session import sessionmaker, Session
from DB_tables import *
from models import *
from random import randint

engine = create_engine('sqlite:///loyalty.db', echo=False, connect_args={'check_same_thread': False})

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def get_user(user_id: int, db: Session):
    db_user = db.query(Users).filter(Users.id == user_id).first()
    return UserModel(
        username=db_user.username,
        points=db_user.balance,
        id=db_user.id,
        avatar=db_user.avatar
    )


def get_products(db: Session):
    db_products = db.query(Products).all()
    products = []
    for db_product in db_products:
        product = ProductModel(id=db_product.id,
                               title=db_product.title,
                               description=db_product.description,
                               img=db_product.img,
                               cost=db_product.cost)
        products.append(product)
    return products


def spend_points(data: Points, db: Session):
    db_product = db.query(Products).filter(Products.id == data.product_id).first()
    stmt = (
        insert(association_table).
            values(user_id=data.user_id, product_id=data.product_id)
    )
    db.execute(stmt)
    db.commit()
    db_user = db.query(Users).filter(Users.id == data.user_id).first()
    db_user.balance -= db_product.cost
    db.commit()
    return db_user.balance


def save_points(user_id: int, db: Session):
    db_user = db.query(Users).filter(Users.id == user_id).first()
    db_user.balance += randint(10, 100)
    db.commit()
    return db_user.balance
