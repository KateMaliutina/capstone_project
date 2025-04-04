from fastapi import FastAPI
from routers import users, skills, vacancies
from routers import recommendations

app = FastAPI()

app.include_router(recommendations.router, prefix="/api", tags=["Recommendations"])
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(skills.router, prefix="/api", tags=["Skills"])
app.include_router(vacancies.router, prefix="/api", tags=["Vacancies"])


@app.get("/")
async def root():
    return {"message": "it works"}
