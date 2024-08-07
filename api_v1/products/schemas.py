from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class UserokBase(BaseModel):
    userokname: str
    userokpass: str


class ProductCreate(ProductBase):
    pass


class UserokCreate(UserokBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None


# Объект для возврата данных
class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)  # чтобы возвращать объекты педантика а не алхимии =(
    id: int


class Userok(UserokBase):
    model_config = ConfigDict(from_attributes=True)  # чтобы возвращать объекты педантика а не алхимии =(
    id: int
