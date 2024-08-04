from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from .base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass

