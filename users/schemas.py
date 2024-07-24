from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Annotated
from annotated_types import MinLen, MaxLen


# Это чтобы педантик там делал свое дело
class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr


# Это тестовая модель не для базы данных
class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True
