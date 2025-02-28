from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from crud import create_vacancy, get_vacancies
from pydantic import BaseModel

router = APIRouter()


# Pydantic-модель для валидации
class VacancyCreate(BaseModel):
    title: str
    description: str
    level: str


# Эндпоинт для создания вакансии
@router.post("/vacancies/")
async def add_vacancy(vacancy: VacancyCreate, db: AsyncSession = Depends(get_db)):
    return await create_vacancy(db, vacancy.title, vacancy.description, vacancy.level)


# Эндпоинт для получения всех вакансий
@router.get("/vacancies/")
async def list_vacancies(db: AsyncSession = Depends(get_db)):
    return await get_vacancies(db)
