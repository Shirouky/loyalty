import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm.session import Session

import crud
from crud import get_db
from models import *

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/spend/points", response_model=float)
async def spend_points(data: Points, db: Session = Depends(get_db)):
    return crud.spend_points(data, db)


@app.post("/save/points/{user_id}", response_model=float)
async def save_points(user_id: int, db: Session = Depends(get_db)):
    return crud.save_points(user_id, db)


@app.get("/user/{user_id}", response_model=UserModel)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(user_id, db)


@app.get("/products", response_model=List[ProductModel])
async def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
