from typing import List

from sqlalchemy import DECIMAL, JSON, Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

association_table = Table(
    "category_film_association",
    Base.metadata,
    Column("film_id", ForeignKey("films.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
)


class Category(IntIdPkMixin, Base):
    __tablename__ = "categories"  # type: ignore
    name: Mapped[str] = mapped_column(unique=True)
    film: Mapped[List["Film"]] = relationship(
        secondary=association_table, back_populates="category"
    )


class Film(IntIdPkMixin, Base):
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    rating: Mapped[float] = mapped_column(DECIMAL(2, 1))
    file_path: Mapped[str] = mapped_column()
    picture_path: Mapped[str] = mapped_column()
    category: Mapped[List[Category]] = relationship(
        secondary=association_table, back_populates="film"
    )
    is_tvshow: Mapped[bool] = mapped_column()
    json_data: Mapped[dict] = mapped_column(JSON(), nullable=True)


class Episode(IntIdPkMixin, Base):
    title: Mapped[str] = mapped_column()
    season: Mapped[int] = mapped_column()
    episode: Mapped[int] = mapped_column()
    file_path: Mapped[str] = mapped_column()
    picture_path: Mapped[str] = mapped_column()
    film_id: Mapped[int] = mapped_column(ForeignKey("films.id"))
    film: Mapped[Film] = relationship("Film")
    category: Mapped[List[Category]] = relationship(
        secondary=association_table, back_populates="film"
    )
