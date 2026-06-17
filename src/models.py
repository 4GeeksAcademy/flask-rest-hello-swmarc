from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from eralchemy2 import render_er

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(120), nullable=False
    )
    firstname: Mapped[str] = mapped_column(
        String(50), nullable=False
    )
    lastname: Mapped[str] = mapped_column(
        String(50), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean(), nullable=False, default=True
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="user"
    )

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }


class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    gender: Mapped[str] = mapped_column(
        String(20), nullable=True
    )

    height: Mapped[str] = mapped_column(
        String(20), nullable=True
    )

    birth_year: Mapped[str] = mapped_column(
        String(20), nullable=True
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="character"
    )


class Planet(db.Model):
    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    climate: Mapped[str] = mapped_column(
        String(100), nullable=True
    )

    terrain: Mapped[str] = mapped_column(
        String(100), nullable=True
    )

    population: Mapped[str] = mapped_column(
        String(100), nullable=True
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="planet"
    )


class Favorite(db.Model):
    __tablename__ = "favorite"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    character_id: Mapped[int] = mapped_column(
        ForeignKey("character.id"),
        nullable=True
    )

    planet_id: Mapped[int] = mapped_column(
        ForeignKey("planet.id"),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="favorites"
    )

    character: Mapped["Character"] = relationship(
        back_populates="favorites"
    )

    planet: Mapped["Planet"] = relationship(
        back_populates="favorites"
    )


if __name__ == "__main__":
    render_er(db.Model, "diagram.png")
