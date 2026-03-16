from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Advertisements API",
    description="Сервис объявлений купли/продажи (учебный проект)",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Добро пожаловать! Перейдите к /docs для документации."}