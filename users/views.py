from fastapi import APIRouter
from .schemas import CreateUser
from users import crud

router = APIRouter(prefix="/users", tags=["Users"])


# Пост запрос с имэйл валидатором от педантика
# Так как это какой-то querystring, FastApi не понимает нихя и ему надо указать
# что мы передаем имэйл именно в теле запроса, для этого нужен объект Body
# все уже не нужен
@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
