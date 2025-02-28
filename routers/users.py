from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from crud import create_user, get_users
from pydantic import BaseModel
from typing import List

router = APIRouter()


# Pydantic-модель для валидации
class UserCreate(BaseModel):
    name: str
    email: str
    level: str
    interests: List[str]


# Эндпоинт для создания пользователя
@router.post("/users/")
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user.name, user.email, user.level, user.interests)


# Эндпоинт для получения всех пользователей
@router.get("/users/")
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)
