from fastapi import APIRouter, Depends, Form, HTTPException, status
from pydantic import BaseModel

from core.schemas.user import UserSchema
from utils import jwt_utils

router = APIRouter(prefix="/jwt", tags=["jwt_auth"])


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


admin = UserSchema(
    username="admin", password=jwt_utils.hash_password("admin"), email="admin@site.com"
)
john = UserSchema(
    username="john", password=jwt_utils.hash_password("password"), email="john@mail.com"
)

users_db: dict[str, UserSchema] = {admin.username: admin, john.username: john}


def validate_auth_user(username: str = Form(), password: str = Form()):
    unauthed_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    if not (user := users_db.get(username)):
        raise unauthed_exception
    if jwt_utils.check_password(password=password, hashed_password=user.password):
        return user
    raise unauthed_exception


@router.post("/login", response_model=TokenInfo)
def auth_user(user: UserSchema = Depends(validate_auth_user)):
    jwt_payload = {
        "sub": user.username,
        "email": user.email,
    }
    token = jwt_utils.encode_jwt({"username": user.username})
    return TokenInfo(access_token=token, token_type="Bearer")
