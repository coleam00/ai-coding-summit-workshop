/**
 * Error types matching backend Pydantic ErrorResponse model EXACTLY.
 *
 * Backend definition (app/models/error.py):
 * ```python
 * class ErrorResponse(BaseModel):
 *     error_code: str = Field(..., min_length=1, max_length=100)
 *     error_message: str = Field(..., min_length=1, max_length=500)
 *     error_details: dict[str, Any] | None = Field(default=None)
 *     timestamp_utc: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())
 * ```
 */

/**
 * Error response model matching backend ErrorResponse.
 *
 * All API errors follow this consistent structure.
 */
export interface ErrorResponse {
  /** Machine-readable error code (e.g., "invalid_price_range", "product_not_found") */
  error_code: string;

  /** Human-readable error message for end users */
  error_message: string;

  /** Optional additional context for debugging */
  error_details?: Record<string, unknown>;

  /** ISO 8601 timestamp when error occurred (UTC) */
  timestamp_utc: string;
}

/**
 * Custom error class for API errors with structured information.
 *
 * Wraps ErrorResponse from backend with HTTP status code.
 * Use this for proper error handling in try-catch blocks.
 *
 * Example:
 * ```typescript
 * try {
 *   await fetchProducts();
 * } catch (error) {
 *   if (error instanceof ApiError) {
 *     console.error(error.errorResponse.error_code);
 *     console.error(error.statusCode);
 *   }
 * }
 * ```
 */
export class ApiError extends Error {
  constructor(
    /** HTTP status code (e.g., 400, 404, 500) */
    public readonly statusCode: number,
    /** Structured error response from backend */
    public readonly errorResponse: ErrorResponse
  ) {
    super(errorResponse.error_message);
    this.name = "ApiError";

    // Maintains proper stack trace for where error was thrown (V8 engines only)
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, ApiError);
    }
  }
}
