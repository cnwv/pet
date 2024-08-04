from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import (
    HTTPBearer,
)
from pydantic import BaseModel
from api.api_v1.auth.helpers import (
    REFRESH_TOKEN_TYPE,
    ACCESS_TOKEN_TYPE,
    TOKEN_TYPE_FIELD,
    create_refresh_token,
    create_access_token,
)
from api.api_v1.auth.validation import (
    get_current_auth_user,
    get_current_auth_user_for_refresh,
    get_current_active_auth_user,
)
from api.api_v1.auth.db import admin, users_db
from core.schemas.user import UserSchema
from utils import jwt_utils

http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix="/jwt", tags=["jwt_auth"], dependencies=[Depends(http_bearer)]
)


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"


def validate_auth_user(
    username: str = Form(..., json_schema_extra={"example": "admin"}),
    password: str = Form(json_schema_extra={"example": "admin"}),
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


@router.get("/refresh", response_model=TokenInfo, response_model_exclude_none=True)
def auth_refresh_jwt(user: UserSchema = Depends(get_current_auth_user_for_refresh)):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return TokenInfo(access_token=access_token, refresh_token=refresh_token)
