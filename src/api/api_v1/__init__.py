from fastapi import APIRouter

# from api.api_v1.auth.auth import router as demo_auth_router
from api.api_v1.auth.test_cookies import router as cookie_router
from api.api_v1.auth_fastapi_users.router import auth_backend, fastapi_users
from core.config import settings

from .auth_fastapi_users.schemas import UserCreate, UserRead, UserUpdate
from .films import router as films_router

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

# router.include_router(
#     demo_auth_router,
# )

router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=False),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate, requires_verification=True),
    prefix="/users",
    tags=["users"],
)
