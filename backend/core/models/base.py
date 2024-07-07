from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase, declared_attr)


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=...  # TODO: Add naming convention
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{...}" # TODO: Add rule for table name

    