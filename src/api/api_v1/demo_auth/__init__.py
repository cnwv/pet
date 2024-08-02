from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
)
from pydantic import BaseModel
from jwt.exceptions import InvalidTokenError

from api.api_v1.demo_auth.helpers import create_access_token, create_refresh_token
from core.schemas.user import UserSchema
from utils import jwt_utils

router = APIRouter(prefix="/jwt", tags=["jwt_auth"])
# http_bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/jwt/login")


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"


admin = UserSchema(
    username="admin", password=jwt_utils.hash_password("admin"), email="admin@site.com"
)
john = UserSchema(
    username="john", password=jwt_utils.hash_password("password"), email="john@mail.com"
)

users_db: dict[str, UserSchema] = {admin.username: admin, john.username: john}


def validate_auth_user(
    username: str = Form(..., example=f"{admin.username}"),
    password: str = Form(..., example=f"{admin.password}"),
):
    unauthed_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    if not (user := users_db.get(username)):
        raise unauthed_exception
    if jwt_utils.check_password(password=password, hashed_password=user.password):
        return user
    # if not user is active raise unauthed_exception
    raise unauthed_exception


@router.post("/login", response_model=TokenInfo)
def auth_user(user: UserSchema = Depends(validate_auth_user)):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return TokenInfo(access_token=access_token, refresh_token=refresh_token)


def get_current_token_payload(
    # credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
    token: str = Depends(oauth2_scheme),
) -> dict:
    try:
        payload = jwt_utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
            # detail=f"invalid token error",
        )
    return payload


def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload),
) -> UserSchema:
    username: str | None = payload.get("sub")
    if users := users_db.get(username):
        return users
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token(user not found)"
    )


def get_current_active_auth_user(
    user: UserSchema = Depends(get_current_auth_user),
) -> UserSchema:
    if user.active:
        return user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")


@router.get("/me")
def auth_user_check_self_info(
    user: UserSchema = Depends(get_current_active_auth_user),
):
    """
    This endpoint is just for demonstration authentication
    """
    return {
        "username": user.username,
        "email": user.email,
    }
