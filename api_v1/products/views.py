from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.userok import Userok
from . import crud
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial, UserokCreate, Userok
from .dependencies import product_by_id

router = APIRouter(tags=["Products"])


# не понимаю, что тут делается вообще
# что-то для тела запроса
@router.get("/", response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.product_create(session=session, product_in=product_in)


@router.post("/userok", response_model=Userok, status_code=status.HTTP_201_CREATED)
async def create_userok(
        userok_in: UserokCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.userok_create(session=session, userok_in=userok_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
        product: Product = Depends(product_by_id),
):
    return product


@router.put("/{product_id}/put")
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch("/{product_id}/")
async def update_product_partial(
        product_update: ProductUpdatePartial,
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@router.delete("/{product_id}/del", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)
