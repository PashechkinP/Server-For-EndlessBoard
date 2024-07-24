from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product  # Добавление аннотации типов
from sqlalchemy.engine import Result  # для аннотирования свойства (что бы это не значило...)
from sqlalchemy import select  # инструмент для создания запросов

from core.models import Userok
from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial, UserokCreate


# Чтение всех товаров ( объявлений для EndlessBoard)
# Принимает объект сессии через который запрашивает данные из бд
async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()  # тюплы,генератор,список - можно выключать и идти спать короче
    return list(products)


# Чтение одного товара
async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


# Создание товара
async def product_create(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())  # словарик распаковывается по ключам
    session.add(product)  # добавление в сессиию для отслеживания, просто надо
    await session.commit()  # сохранение товара в базу данных
    # await session.refresh(product)
    return product


async def userok_create(session: AsyncSession, userok_in: UserokCreate) -> Userok:
    userok = Userok(**userok_in.model_dump())  # словарик распаковывается по ключам
    session.add(userok)  # добавление в сессиию для отслеживания, просто надо
    await session.commit()  # сохранение товара в базу данных
    # await session.refresh(product)
    return userok


# Это апдейт всего объекта
# async def update_product(
#         session: AsyncSession,
#         product: Product,
#         product_update: ProductUpdate | ProductUpdatePartial,
#         partial: bool = False,
# ) -> Product:
#     for name, value in product_update.model_dump(exclude_unset=partial).items():
#         setattr(product, name, value)
#     await session.commit()
#     return product
#
#
# Это апдейт конкретных полей объекта
# async def update_product_partial(
#         session: AsyncSession,
#         product: Product,
#         product_update: ProductUpdatePartial,
#         partial: bool = False,
# ) -> Product:
#     for name, value in product_update.model_dump(exclude_unset=True).items():
#         setattr(product, name, value)
#     await session.commit()
#     return product


# Это гибрид верхних двух
async def update_product(
        session: AsyncSession,
        product: Product,
        product_update: ProductUpdate | ProductUpdatePartial,
        partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
        session: AsyncSession,
        product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
