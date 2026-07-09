from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)

    company: Mapped[str] = mapped_column(String(255), nullable=False)

    location: Mapped[str] = mapped_column(String(255), nullable=False)

    salary: Mapped[str | None] = mapped_column(String(255))

    url: Mapped[str] = mapped_column(Text, unique=True, nullable=False)

    description: Mapped[str | None] = mapped_column(Text)

    source: Mapped[str] = mapped_column(String(50), nullable=False)

    posted_date: Mapped[str | None] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )