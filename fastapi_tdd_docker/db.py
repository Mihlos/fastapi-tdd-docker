import os

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["fastapi_tdd_docker.models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}
