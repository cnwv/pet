from core.schemas.user import UserSchema
from utils import jwt_utils


def create_token(user: UserSchema) -> str:
    pass


def create_access_token(user: UserSchema) -> str:
    jwt_payload = {
        "sub": user.username,
        "email": user.email,
    }
    return jwt_utils.encode_jwt(jwt_payload)


def create_refresh_token(user: UserSchema) -> str:

    return jwt_utils.encode_jwt(jwt_payload)
