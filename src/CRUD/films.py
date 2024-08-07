from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Category, Film

# from core.schemas.films import UserCreate


async def get_all_films(
    session: AsyncSession,
) -> Sequence[Film]:
    stmt = select(Film)
    result = await session.scalars(stmt)
    return result.all()


async def get_all_categories(
    session: AsyncSession,
) -> Sequence[Category]:
    stmt = select(Category)
    result = await session.scalars(stmt)
    return result.all()


async def get_film_by_id(
    session: AsyncSession,
    film_id,
) -> Sequence[Film] | None:
    stmt = select(Film).where(Film.id == film_id)
    if result := await session.scalar(stmt):
        return result
    return None
