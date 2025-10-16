/**
 * ProductCard component for displaying a single product.
 *
 * Uses shadcn Card component for consistent styling and layout.
 * Displays all product information with proper formatting and badges.
 *
 * Backend model (app/models/product.py):
 * ```python
 * class Product(BaseModel):
 *     product_id: int
 *     product_name: str
 *     product_description: str
 *     product_price_usd: Decimal
 *     product_category: ProductCategory
 *     product_in_stock: bool
 * ```
 */

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import type { Product } from "@/types/product";

interface ProductCardProps {
  /** Product object to display (matches backend Product model) */
  product: Product;
}

/**
 * Display a single product in a card layout.
 *
 * Features:
 * - Product name and description
 * - Formatted price in USD
 * - Category badge with color coding
 * - Stock status indicator
 * - Responsive layout
 *
 * @param product - Product data from API
 */
export function ProductCard({ product }: ProductCardProps) {
  // Format price as USD currency
  // Backend sends Decimal as string, parse to number for formatting
  const formattedPrice = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(parseFloat(product.product_price_usd));

  // Category badge color mapping
  // Each category gets a distinct color for visual distinction
  const categoryColors: Record<string, string> = {
    electronics: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
    clothing: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200",
    home: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
    sports: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
    books: "bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200",
  };

  const categoryColor = categoryColors[product.product_category] || "bg-gray-100 text-gray-800";

  return (
    <Card className="h-full flex flex-col transition-shadow hover:shadow-lg">
      <CardHeader>
        <div className="flex items-start justify-between gap-2">
          <CardTitle className="text-lg line-clamp-2 flex-1">{product.product_name}</CardTitle>
          <span className={`px-2 py-1 text-xs font-medium rounded-md whitespace-nowrap ${categoryColor}`}>
            {product.product_category}
          </span>
        </div>
      </CardHeader>
      <CardContent className="flex-1 flex flex-col">
        {/* Product description with line clamping */}
        <p className="text-sm text-muted-foreground line-clamp-3 mb-4">{product.product_description}</p>

        {/* Price and stock status - pushed to bottom */}
        <div className="mt-auto flex items-center justify-between pt-4 border-t">
          <span className="text-2xl font-bold">{formattedPrice}</span>
          {product.product_in_stock ? (
            <span className="text-sm text-green-600 dark:text-green-400 font-medium flex items-center gap-1">
              <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" role="img" aria-label="In stock">
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                  clipRule="evenodd"
                />
              </svg>
              In Stock
            </span>
          ) : (
            <span className="text-sm text-red-600 dark:text-red-400 font-medium flex items-center gap-1">
              <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" role="img" aria-label="Out of stock">
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clipRule="evenodd"
                />
              </svg>
              Out of Stock
            </span>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
