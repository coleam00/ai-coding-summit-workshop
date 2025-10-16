"""
Main FastAPI application entry point.

This module initializes the FastAPI app, configures middleware,
sets up logging, and registers all API routers.
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import products
from app.core.config import settings
from app.core.logging_config import StructuredLogger, setup_logging

# Configure structured JSON logging
setup_logging(log_level=settings.log_level)

# Initialize logger for this module
logger = StructuredLogger(__name__)


@asynccontextmanager
async def application_lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Manage application lifespan events (startup and shutdown).

    This context manager handles initialization on startup and cleanup on shutdown,
    logging both events for monitoring and debugging purposes.

    Args:
        app: The FastAPI application instance

    Yields:
        None: Control flow during application runtime
    """
    # Startup: Log application initialization
    logger.info(
        "application_startup",
        application_name=settings.application_name,
        application_version=settings.application_version,
        log_level=settings.log_level,
        cors_enabled=settings.enable_cors,
    )

    yield

    # Shutdown: Log application termination
    logger.info("application_shutdown", application_name=settings.application_name)


# Create FastAPI application instance with lifespan handler
app = FastAPI(
    title=settings.application_name,
    version=settings.application_version,
    description="E-commerce product catalog API with filtering and search capabilities",
    lifespan=application_lifespan,
)

# Configure CORS (Cross-Origin Resource Sharing) if enabled
if settings.enable_cors:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify exact origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    logger.info("cors_middleware_enabled", allow_origins="*", allow_methods="*")

# Register API routers
app.include_router(products.router)
logger.info("api_router_registered", router_prefix="/api/products", router_tag="products")


@app.get("/health")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint for monitoring and load balancers.

    Returns:
        Dictionary with status indicating the application is running

    Example Response:
        {"status": "healthy"}
    """
    logger.info("health_check_request", endpoint="/health")

    return {"status": "healthy"}
