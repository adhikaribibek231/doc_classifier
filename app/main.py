from fastapi import FastAPI
from app.core.config import settings
from contextlib import asynccontextmanager
from app.core.logging import get_logger
from app.api.v1.routes import router as api_router

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up the application...")
    yield
    logger.info("Shutting down the application...")
    
def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    logger.info(f"Application '{settings.app_name}' created.")
    app.include_router(api_router, prefix="/api/v1")
    logger.info("API routes included. at /api/v1")
    return app

app = create_app()

