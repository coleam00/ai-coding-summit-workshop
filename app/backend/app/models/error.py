"""Error response models for consistent API error handling."""

from datetime import UTC, datetime
from typing import Any

from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    """
    Standard error response format for all API errors.

    This model ensures consistent error messaging across the entire API,
    making it easier for both humans and AI to understand what went wrong.

    Attributes:
        error_code: Machine-readable error identifier (e.g., 'invalid_price_range')
        error_message: Human-readable error message for end users
        error_details: Optional dictionary with additional debugging context
        timestamp_utc: ISO 8601 formatted timestamp when the error occurred

    Examples:
        >>> ErrorResponse(
        ...     error_code="invalid_price_range",
        ...     error_message="Minimum price cannot exceed maximum price",
        ...     error_details={"min_price": "100.00", "max_price": "50.00"}
        ... )
    """

    error_code: str = Field(
        ...,
        description="Machine-readable error code for programmatic handling",
        examples=["invalid_price_range", "product_not_found", "validation_error"],
        min_length=1,
        max_length=100,
    )

    error_message: str = Field(
        ...,
        description="Human-readable error message suitable for displaying to end users",
        min_length=1,
        max_length=500,
    )

    error_details: dict[str, Any] | None = Field(
        default=None, description="Additional context about the error for debugging purposes"
    )

    timestamp_utc: str = Field(
        default_factory=lambda: datetime.now(UTC).isoformat(),
        description="ISO 8601 timestamp when the error occurred (UTC timezone)",
    )
