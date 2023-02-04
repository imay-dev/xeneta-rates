from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.config import Settings, get_settings

router = APIRouter()

class Ping(BaseModel):
    ping: str = 'pong'
    environment: str = 'dev'
    testing: bool = True


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)) -> Ping :
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
