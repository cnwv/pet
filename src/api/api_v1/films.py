from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.films import FilmRead
from CRUD.films import get_all_categories, get_all_films, get_film_by_id

router = APIRouter(tags=["Films"])


@router.get("", response_model=list[FilmRead])
async def get_films(session: AsyncSession = Depends(db_helper.session_getter)):
    films = await get_all_films(session)
    return films


@router.get("/categories")
async def get_categories(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    categories = await get_all_categories(session)
    return categories


@router.get("/{film_id}", response_model=FilmRead | None)
async def get_film(
    film_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    film = await get_film_by_id(session, film_id)
    return film
