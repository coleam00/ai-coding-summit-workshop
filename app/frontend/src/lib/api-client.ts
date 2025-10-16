/**
 * Type-safe API client for communicating with FastAPI backend.
 *
 * Backend endpoints (app/api/products.py, app/main.py):
 * - GET /api/products - Get all products
 * - GET /health - Health check
 *
 * Configuration:
 * - API_BASE_URL: Backend URL from environment or default
 *
 * Error handling:
 * - Network errors: Throws standard Error
 * - API errors: Throws ApiError with ErrorResponse
 */

import { ApiError, type ErrorResponse } from "@/types/error";
import type { ProductListResponse } from "@/types/product";
import { logger } from "./logger";

/**
 * Backend API base URL.
 *
 * Default: http://localhost:8000 (matching backend run_api.py port)
 * TODO: Make this configurable via build-time environment variable
 */
const API_BASE_URL = "http://localhost:8000";

/**
 * Fetch all products from the catalog API.
 *
 * Backend endpoint: GET /api/products
 * Response model: ProductListResponse
 *
 * @returns ProductListResponse with products array and total count
 * @throws ApiError if backend returns error response (4xx/5xx)
 * @throws Error if network failure or unable to reach backend
 *
 * Example usage:
 * ```typescript
 * try {
 *   const response = await fetchProducts();
 *   console.log(`Loaded ${response.total_count} products`);
 * } catch (error) {
 *   if (error instanceof ApiError) {
 *     console.error(`API Error: ${error.errorResponse.error_code}`);
 *   } else {
 *     console.error('Network error');
 *   }
 * }
 * ```
 */
export async function fetchProducts(): Promise<ProductListResponse> {
  const endpoint = "/api/products";
  const url = `${API_BASE_URL}${endpoint}`;

  logger.info("fetching_products", {
    endpoint,
    url,
    operation: "fetchProducts",
  });

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    // Handle non-OK responses (4xx, 5xx)
    if (!response.ok) {
      let errorData: ErrorResponse;

      try {
        // Try to parse error response from backend
        errorData = await response.json();
      } catch {
        // Fallback if response isn't JSON
        errorData = {
          error_code: "unknown_error",
          error_message: `HTTP ${response.status}: ${response.statusText}`,
          timestamp_utc: new Date().toISOString(),
        };
      }

      logger.error("fetch_products_failed", {
        endpoint,
        status_code: response.status,
        error_code: errorData.error_code,
        error_message: errorData.error_message,
        operation: "fetchProducts",
      });

      throw new ApiError(response.status, errorData);
    }

    // Parse successful response
    const data: ProductListResponse = await response.json();

    logger.info("products_fetched_successfully", {
      endpoint,
      products_count: data.total_count,
      operation: "fetchProducts",
    });

    return data;
  } catch (error) {
    // Re-throw ApiError as-is
    if (error instanceof ApiError) {
      throw error;
    }

    // Handle network errors (fetch failed completely)
    const errorMessage = error instanceof Error ? error.message : String(error);

    logger.error("network_error", {
      endpoint,
      error_message: errorMessage,
      error_type: "network_failure",
      fix_suggestion: `Check that backend server is running at ${API_BASE_URL}`,
      operation: "fetchProducts",
    });

    throw new Error(`Network error while fetching products: ${errorMessage}`);
  }
}

/**
 * Health check for the backend API.
 *
 * Backend endpoint: GET /health
 * Expected response: { "status": "healthy" }
 *
 * @returns true if backend is healthy and reachable
 * @returns false if backend is down or unhealthy
 *
 * Example usage:
 * ```typescript
 * const isHealthy = await checkHealth();
 * if (!isHealthy) {
 *   console.warn('Backend is not responding');
 * }
 * ```
 */
export async function checkHealth(): Promise<boolean> {
  const endpoint = "/health";
  const url = `${API_BASE_URL}${endpoint}`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      return false;
    }

    const data = await response.json();
    const isHealthy = data.status === "healthy";

    logger.info("health_check_completed", {
      endpoint,
      is_healthy: isHealthy,
      operation: "checkHealth",
    });

    return isHealthy;
  } catch (error) {
    logger.warning("health_check_failed", {
      endpoint,
      error_message: error instanceof Error ? error.message : String(error),
      operation: "checkHealth",
    });

    return false;
  }
}
