from fastapi import APIRouter
from app.core.logging import get_logger
from app.api.v1.ingestion import router as ingestion_router

logger = get_logger(__name__)
router = APIRouter()
router.include_router(ingestion_router, prefix="/ingestion", tags=["ingestion"])

@router.get("/health")
async def health_check():
    """Health check endpoint.

    Returns:
        dict: Health status information.
    """
    logger.info("health_check_called")
    return {"status": "healthy", "version": "1.0.0"}
