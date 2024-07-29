from fastapi import APIRouter

from .films import router as films_router
from core.config import settings
from api.api_v1.demo_auth import router as demo_auth_router
from api.api_v1.demo_auth.test_cookies import router as cookie_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    films_router,
    prefix=settings.api.v1.films,
)
router.include_router(
    cookie_router,
    prefix="/cookie",
)

router.include_router(
    demo_auth_router,
)
