from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Annotated # Правила заполнения всякие
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from core.config import settings
from core.models import Base, db_helper
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router

# Так через асинхронный движок будет выполненно создание таблиц при запуске проги
@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "https://127.0.0.1",
    "http://127.0.0.1:8000/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
    expose_headers=["*"]
)


@app.get("/")
def hello():
    return {
        "message": "hello index!",
    }


# Обработка запроса с параметром
@app.get("/hello/")
def hello(name: str = "Universe"): # = "universe" если не передали параметров то по умолчанию значение
    name = name.strip().title()   #strip удаляет лишние пробелы title делает первую заглавной
    return {"message": f"hello {name}"}



# для автоматического перезапуска серва при изменениях кода
if __name__ == '_main_':
    uvicorn.run("main:app",reload=True)