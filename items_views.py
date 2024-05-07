from fastapi import APIRouter, Path
from typing import Annotated

# Чтобы убрать @app ошибку
router = APIRouter(prefix="/items", tags=["Items"]) # префикс везде добавляется в путь,tags-группировка в swagger

# json строка
@router.get("/")
def list_items():
    return [
        "item1",
        "item2",
        "item3",
    ]

# Важен порядок расположения в коде этих запросов
# Если поставить этот запрос после /{items_id}/ запроса и попробовать вернуть строку
# то будет выполняться сначала запрос /{items_id}/ интовый и выдавать ошибку
@router.get("/latest/")
def get_latest_item():
    return {
        "item":{"id": "0", "name": "latest"}
    }

# это словарь
@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item":{
            "id": item_id,
        },
    }
