"""
Product API endpoints.

This module defines all HTTP endpoints related to product operations.
Each endpoint delegates business logic to the service layer.
"""

from fastapi import APIRouter

from app.core.logging_config import StructuredLogger
from app.models.product import ProductListResponse
from app.services import product_service

# Initialize router for product endpoints
router = APIRouter(prefix="/api/products", tags=["products"])

# Initialize structured logger
logger = StructuredLogger(__name__)


@router.get("", response_model=ProductListResponse)
async def get_products() -> ProductListResponse:
    """
    Get all products from the catalog.

    This endpoint returns all products currently available in the catalog.
    In the future, this endpoint will support filtering by price, category,
    and keyword search (that's what you'll be adding in the exercise!).

    Returns:
        ProductListResponse containing list of products and total count

    Example Response:
        {
            "products": [
                {
                    "product_id": 1,
                    "product_name": "Wireless Bluetooth Mouse",
                    "product_description": "Ergonomic wireless mouse...",
                    "product_price_usd": "29.99",
                    "product_category": "electronics",
                    "product_in_stock": true
                },
                ...
            ],
            "total_count": 30
        }
    """
    logger.info("api_request_received", endpoint="/api/products", http_method="GET", operation="get_products")

    # Delegate to service layer for business logic
    products = product_service.get_all_products()

    logger.info(
        "api_response_prepared", endpoint="/api/products", products_count=len(products), operation="get_products"
    )

    return ProductListResponse(products=products, total_count=len(products))
