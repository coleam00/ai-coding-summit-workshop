/**
 * Structured logging utility matching backend logging patterns.
 *
 * This mirrors the backend's StructuredLogger (app/core/logging_config.py).
 * Logs are output as JSON to console for AI readability and debugging.
 *
 * Backend pattern:
 * ```python
 * logger = StructuredLogger(__name__)
 * logger.info("filtering_products", filter_category="electronics", total_products=30)
 * ```
 *
 * Frontend usage:
 * ```typescript
 * import { logger } from "@/lib/logger";
 * logger.info("fetching_products", { endpoint: "/api/products", operation: "initial_load" });
 * ```
 *
 * Key principles for AI-friendly logging (matching backend):
 * 1. Use JSON format for machine readability
 * 2. Include contextual fields (operation, parameters, results)
 * 3. Log to console (AI can read it directly)
 * 4. Use descriptive event names (fetching_products, validation_failed, etc.)
 * 5. Include fix_suggestion fields in error logs where appropriate
 */

/** Log data structure for additional context fields */
interface LogData {
  [key: string]: unknown;
}

/**
 * StructuredLogger class for consistent JSON logging.
 *
 * Mirrors backend StructuredLogger pattern but adapted for frontend/console.
 *
 * Output format matches backend:
 * {
 *   "timestamp": "2025-10-13T13:14:03.123Z",
 *   "level": "INFO",
 *   "logger_name": "frontend",
 *   "message": "fetching_products",
 *   ...additional_fields
 * }
 */
class StructuredLogger {
  /**
   * Format log entry as JSON string.
   *
   * @param level - Log level (INFO, ERROR, WARNING, DEBUG)
   * @param message - Event name or message (use snake_case like backend)
   * @param data - Additional structured fields
   */
  private formatLog(level: string, message: string, data?: LogData): string {
    return JSON.stringify({
      timestamp: new Date().toISOString(),
      level,
      logger_name: "frontend",
      message,
      ...data,
    });
  }

  /**
   * Log informational message.
   *
   * Use for normal operations like API calls, state changes, etc.
   *
   * Example:
   * ```typescript
   * logger.info("fetching_products", {
   *   endpoint: "/api/products",
   *   operation: "initial_load"
   * });
   * ```
   */
  info(message: string, data?: LogData): void {
    console.log(this.formatLog("INFO", message, data));
  }

  /**
   * Log error message.
   *
   * Use for errors, failures, exceptions.
   * Include fix_suggestion field when possible (matching backend pattern).
   *
   * Example:
   * ```typescript
   * logger.error("fetch_products_failed", {
   *   error_message: err.message,
   *   status_code: 500,
   *   fix_suggestion: "Check backend server is running"
   * });
   * ```
   */
  error(message: string, data?: LogData): void {
    console.error(this.formatLog("ERROR", message, data));
  }

  /**
   * Log warning message.
   *
   * Use for recoverable issues, deprecations, etc.
   *
   * Example:
   * ```typescript
   * logger.warning("api_slow_response", {
   *   endpoint: "/api/products",
   *   response_time_ms: 5000
   * });
   * ```
   */
  warning(message: string, data?: LogData): void {
    console.warn(this.formatLog("WARNING", message, data));
  }

  /**
   * Log debug message.
   *
   * Use for development/debugging information.
   *
   * Example:
   * ```typescript
   * logger.debug("state_updated", {
   *   previous_count: 0,
   *   new_count: 30
   * });
   * ```
   */
  debug(message: string, data?: LogData): void {
    console.debug(this.formatLog("DEBUG", message, data));
  }
}

/** Singleton logger instance for use throughout the application */
export const logger = new StructuredLogger();
