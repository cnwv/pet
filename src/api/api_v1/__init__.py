from fastapi import APIRouter

from .films import router as films_router
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    films_router,
    prefix=settings.api.v1.films,
)
