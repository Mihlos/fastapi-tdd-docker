import os

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from fastapi_tdd_docker.config import get_settings, Settings

app = FastAPI()


register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["fastapi_tdd_docker.models.tortoise"]},
    generate_schemas=False,
    add_exception_handlers=True,
)


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pongus",
        "environment": settings.environment,
        "testing": settings.testing,
    }
