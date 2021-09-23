from fastapi import APIRouter

from app.models.user import User
from app.database.db import conn
from app.schemas.user import userEntity, usersEntity

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    
    return usersEntity(conn.local.user.find())