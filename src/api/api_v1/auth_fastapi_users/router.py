import uuid

from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    BearerTransport,
    JWTStrategy,
    AuthenticationBackend,
)

from api.api_v1.auth_fastapi_users.user_manager import get_user_manager
from core.config import settings
from core.models import User

bearer_transport = BearerTransport(tokenUrl="api/v1/auth/jwt/login")

api_router = APIRouter(prefix="/auth-v2", tags=["fastapi_users"])


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.auth_jwt.private_key_path.read_text(),
        lifetime_seconds=3600,
        algorithm="RS256",
        public_key=settings.auth_jwt.public_key_path.read_text(),
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


@api_router.get("")
def get():
    return 200
