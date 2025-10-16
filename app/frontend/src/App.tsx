/**
 * Main application component for the Product Catalog.
 *
 * Responsibilities:
 * - Fetch products from backend API on mount
 * - Manage loading, error, and success states
 * - Display product grid with proper error handling
 * - Provide user feedback for all states
 *
 * State management:
 * - products: Array of Product objects from API
 * - loading: Boolean indicating API call in progress
 * - error: String with error message (null if no error)
 *
 * Backend integration:
 * - Calls GET /api/products via fetchProducts()
 * - Handles ApiError and network errors
 * - Logs all operations for debugging
 */

import { useCallback, useEffect, useState } from "react";
import { ProductGrid } from "@/components/ProductGrid";
import { fetchProducts } from "@/lib/api-client";
import { logger } from "@/lib/logger";
import { ApiError } from "@/types/error";
import type { Product } from "@/types/product";
import "./index.css";

/**
 * Main App component.
 *
 * Lifecycle:
 * 1. Mount: Start loading products
 * 2. Loading: Show loading spinner in ProductGrid
 * 3. Success: Display products in grid
 * 4. Error: Show error message with retry button
 */
export function App() {
  // State for products data
  const [products, setProducts] = useState<Product[]>([]);

  // State for loading indicator
  const [loading, setLoading] = useState<boolean>(true);

  // State for error message (null = no error)
  const [error, setError] = useState<string | null>(null);

  /**
   * Fetch products from backend API.
   *
   * Handles both ApiError (from backend) and network errors.
   * Updates state based on result.
   */
  const loadProducts = useCallback(async () => {
    logger.info("app_loading_products", {
      operation: "initial_load",
      component: "App",
    });

    try {
      setLoading(true);
      setError(null);

      // Call backend API
      const response = await fetchProducts();

      // Update state with fetched products
      setProducts(response.products);

      logger.info("app_products_loaded", {
        products_count: response.total_count,
        operation: "initial_load",
        component: "App",
      });
    } catch (err) {
      // Extract error message based on error type
      const errorMessage =
        err instanceof ApiError
          ? err.errorResponse.error_message
          : err instanceof Error
            ? err.message
            : "An unknown error occurred while loading products";

      setError(errorMessage);

      logger.error("app_load_products_failed", {
        error_message: errorMessage,
        error_type: err instanceof ApiError ? "api_error" : "network_error",
        error_code: err instanceof ApiError ? err.errorResponse.error_code : undefined,
        operation: "initial_load",
        component: "App",
        fix_suggestion:
          err instanceof ApiError
            ? "Check backend logs for error details"
            : "Verify backend server is running at http://localhost:8000",
      });
    } finally {
      setLoading(false);
    }
  }, []);

  // Load products on component mount
  useEffect(() => {
    loadProducts();
  }, [loadProducts]);

  return (
    <div className="min-h-screen bg-background">
      {/* Header section */}
      <header className="border-b bg-card/50 backdrop-blur-sm sticky top-0 z-10">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold">Product Catalog</h1>
          <p className="text-muted-foreground mt-1">
            {loading
              ? "Loading products..."
              : error
                ? "Error loading products"
                : `Browse our collection of ${products.length} products`}
          </p>
        </div>
      </header>

      {/* Main content area */}
      <main className="container mx-auto px-4 py-8">
        {/* Error state - show error message with retry button */}
        {error ? (
          <div className="max-w-2xl mx-auto">
            <div className="bg-destructive/10 border border-destructive text-destructive px-6 py-4 rounded-lg">
              <div className="flex items-start gap-3">
                {/* Error icon */}
                <svg
                  className="w-6 h-6 flex-shrink-0 mt-0.5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  role="img"
                  aria-label="Error"
                >
                  <path
                    fillRule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                    clipRule="evenodd"
                  />
                </svg>
                <div className="flex-1">
                  <p className="font-semibold text-lg">Error loading products</p>
                  <p className="text-sm mt-1">{error}</p>
                  <button
                    type="button"
                    onClick={loadProducts}
                    className="mt-3 text-sm underline hover:no-underline font-medium"
                  >
                    Try again
                  </button>
                </div>
              </div>
            </div>

            {/* Helpful debug info */}
            <div className="mt-4 text-sm text-muted-foreground text-center">
              <p>Make sure the backend server is running:</p>
              <code className="block mt-1 bg-muted px-2 py-1 rounded text-xs">
                cd app/backend && uv run python run_api.py
              </code>
            </div>
          </div>
        ) : (
          // Success/Loading state - show product grid
          <ProductGrid products={products} loading={loading} />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t mt-12 py-6">
        <div className="container mx-auto px-4 text-center text-sm text-muted-foreground">
          <p>Product Catalog API - Module 1 Exercise</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
