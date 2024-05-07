from .schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()  # Делаем словарик из этих данных
    return {
        "success": True,
        "user": user,
    }
