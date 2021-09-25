from fastapi import APIRouter

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List

from app.models import models
from app.database.db import db

router = APIRouter(
    prefix="/users",
    tags=["users"],    
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=List[models.UserResponse])
async def find_all_users():
    users = await db["users"].find().to_list(1000)
    return users

@router.post('/', response_description="Add new user", response_model=models.User)
async def create_user(user: models.User = Body(...)):
    user = jsonable_encoder(user)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


