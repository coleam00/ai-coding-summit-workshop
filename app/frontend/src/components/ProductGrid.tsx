/**
 * ProductGrid component for displaying a responsive grid of products.
 *
 * Handles three states:
 * 1. Loading - Shows spinner and loading message
 * 2. Empty - Shows message when no products match criteria
 * 3. Success - Shows grid of ProductCard components
 *
 * Layout:
 * - 1 column on mobile
 * - 2 columns on tablets (md breakpoint)
 * - 3 columns on desktop (lg breakpoint)
 */

import type { Product } from "@/types/product";
import { ProductCard } from "./ProductCard";

interface ProductGridProps {
  /** Array of products to display */
  products: Product[];

  /** Whether products are currently being loaded from API */
  loading: boolean;
}

/**
 * Display products in a responsive grid layout.
 *
 * @param products - Products array from ProductListResponse
 * @param loading - Loading state from parent component
 */
export function ProductGrid({ products, loading }: ProductGridProps) {
  // Loading state - show spinner
  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <div className="text-center">
          {/* Animated spinner */}
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4" />
          <p className="text-muted-foreground">Loading products...</p>
        </div>
      </div>
    );
  }

  // Empty state - no products found
  if (products.length === 0) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <div className="text-center max-w-md">
          {/* Empty state illustration */}
          <svg
            className="mx-auto h-24 w-24 text-muted-foreground/50 mb-4"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            aria-hidden="true"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
            />
          </svg>
          <h3 className="text-xl font-semibold mb-2">No products found</h3>
          <p className="text-muted-foreground">Try adjusting your filters or check back later for new products.</p>
        </div>
      </div>
    );
  }

  // Success state - show product grid
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {products.map((product) => (
        <ProductCard key={product.product_id} product={product} />
      ))}
    </div>
  );
}
