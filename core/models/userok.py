from sqlalchemy.orm import Mapped

from .base import Base


class Userok(Base):
    __tablename__ = "userki"

    userokname: Mapped[str]
    userokpass: Mapped[str]
