from core.schemas.user import UserSchema
from utils import jwt_utils

admin = UserSchema(
    username="admin",
    password=jwt_utils.hash_password("admin"),
    email="admin@site.com",
)
john = UserSchema(
    username="john",
    password=jwt_utils.hash_password("password"),
    email="john@mail.com",
)
users_db: dict[str, UserSchema] = {admin.username: admin, john.username: john}
