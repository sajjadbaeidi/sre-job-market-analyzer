from fastapi import APIRouter
from sqlalchemy import text

from src.common.database import engine

router = APIRouter()


@router.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as exc:
        return {
            "status": "unhealthy",
            "database": str(exc),
        }