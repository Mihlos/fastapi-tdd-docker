from fastapi import FastAPI
from fastapi.params import Depends
from fastapi_tdd_docker.config import get_settings, Settings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pongus",
        "environment": settings.environment,
        "testing": settings.testing,
    }
