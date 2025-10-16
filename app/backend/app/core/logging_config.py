"""
Structured JSON logging configuration for AI-debuggable output.

This module configures logging to output structured JSON to stdout, making it
easy for AI coding assistants to read and understand errors, debugging context,
and application behavior.

Key principles for AI-friendly logging:
1. Use JSON format for machine readability
2. Include contextual fields (operation, parameters, results)
3. Log to stdout (AI can read it directly)
4. Use descriptive event names (filtering_products, validation_failed, etc.)
5. Include fix_suggestion fields in error logs
"""

import json
import logging
import sys
from datetime import UTC, datetime
from typing import Any


class JsonFormatter(logging.Formatter):
    """
    Formats log records as JSON objects for structured logging.

    Each log record is converted to a JSON object with:
    - timestamp: ISO 8601 formatted UTC timestamp
    - level: Log level (INFO, ERROR, WARNING, etc.)
    - logger_name: Name of the logger that generated the record
    - message: The log message
    - **extra_fields: Any additional context passed via extra={}

    Example output:
        {
            "timestamp": "2025-01-15T10:30:45.123456Z",
            "level": "INFO",
            "logger_name": "app.services.product_service",
            "message": "filtering_products",
            "filter_category": "electronics",
            "total_products": 30
        }
    """

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record as a JSON string.

        Args:
            record: The log record to format

        Returns:
            JSON-formatted string representation of the log record
        """
        log_data: dict[str, Any] = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "logger_name": record.name,
            "message": record.getMessage(),
        }

        # Add any extra fields that were passed to the logger
        # (e.g., logger.info("event", extra={"field": "value"}))
        if hasattr(record, "extra_fields"):
            log_data.update(record.extra_fields)  # type: ignore[attr-defined]

        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_data, default=str)


def setup_logging(log_level: str = "INFO") -> None:
    """
    Configure application-wide structured JSON logging to stdout.

    This function sets up all loggers to output JSON-formatted logs to stdout,
    making it easy for AI to read and understand application behavior.

    Args:
        log_level: The minimum log level to output (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Example:
        >>> setup_logging("INFO")
        >>> logger = logging.getLogger(__name__)
        >>> logger.info(
        ...     "Processing products",
        ...     extra={"total_products": 30, "filter_category": "electronics"}
        ... )
    """
    # Create JSON formatter
    json_formatter = JsonFormatter()

    # Configure stdout handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(json_formatter)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level.upper()))
    root_logger.addHandler(stdout_handler)

    # Prevent duplicate logs from propagating
    root_logger.propagate = False


def get_logger(logger_name: str) -> logging.Logger:
    """
    Get a configured logger instance with structured logging support.

    This is a convenience function that returns a logger configured for
    JSON output. Use extra={} to add structured fields to your logs.

    Args:
        logger_name: Name for the logger (typically __name__)

    Returns:
        Configured logger instance

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info(
        ...     "filtering_products",
        ...     extra={
        ...         "filter_category": "electronics",
        ...         "min_price": "10.00",
        ...         "max_price": "100.00"
        ...     }
        ... )

        >>> logger.error(
        ...     "validation_failed",
        ...     extra={
        ...         "error_type": "invalid_price_range",
        ...         "error_details": {"min_price": "100", "max_price": "50"},
        ...         "fix_suggestion": "Ensure min_price_usd <= max_price_usd"
        ...     }
        ... )
    """
    return logging.getLogger(logger_name)


# Custom adapter for cleaner API
class StructuredLogger:
    """
    Logger wrapper that makes structured logging more ergonomic.

    Instead of passing extra={} every time, this wrapper lets you pass
    fields directly as keyword arguments.

    Example:
        >>> logger = StructuredLogger(__name__)
        >>> logger.info(
        ...     "filtering_products",
        ...     filter_category="electronics",
        ...     total_products=30
        ... )
    """

    def __init__(self, logger_name: str):
        """Initialize with a logger name."""
        self._logger = logging.getLogger(logger_name)

    def _log(self, level: int, message: str, **fields: Any) -> None:
        """Internal method to log with structured fields."""
        # Create a modified record that includes our fields
        record = self._logger.makeRecord(
            self._logger.name,
            level,
            "",  # pathname
            0,  # lineno
            message,
            (),  # args
            None,  # exc_info
        )
        record.extra_fields = fields
        self._logger.handle(record)

    def debug(self, message: str, **fields: Any) -> None:
        """Log a debug message with structured fields."""
        self._log(logging.DEBUG, message, **fields)

    def info(self, message: str, **fields: Any) -> None:
        """Log an info message with structured fields."""
        self._log(logging.INFO, message, **fields)

    def warning(self, message: str, **fields: Any) -> None:
        """Log a warning message with structured fields."""
        self._log(logging.WARNING, message, **fields)

    def error(self, message: str, **fields: Any) -> None:
        """Log an error message with structured fields."""
        self._log(logging.ERROR, message, **fields)

    def critical(self, message: str, **fields: Any) -> None:
        """Log a critical message with structured fields."""
        self._log(logging.CRITICAL, message, **fields)
