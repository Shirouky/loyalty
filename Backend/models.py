from pydantic import BaseModel
from typing import List, Optional


class ProductModel(BaseModel):
    id: int
    title: str
    description: str
    img: str
    cost: float


class UserModel(BaseModel):
    id: int
    username: str
    points: float
    avatar: str


class Points(BaseModel):
    date: str
    user_id: int
    product_id: int
