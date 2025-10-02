from logging import INFO, basicConfig

from app.config import settings

basicConfig(level=INFO, format="[%(asctime)s - %(name)s] (%(levelname)s) %(message)s")

api = FastAPI(title=settings.api_name)


@api.get("/")
async def root() -> dict[str, str]:
    return {"message": "Server is running!"}


