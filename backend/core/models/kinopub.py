from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class Category(IntIdPkMixin, Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(unique=True)


class Film(IntIdPkMixin, Base):
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship()
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
