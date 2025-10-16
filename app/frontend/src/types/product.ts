/**
 * Product types matching backend Pydantic models EXACTLY.
 *
 * Backend definitions (app/models/product.py):
 * - ProductCategory = Literal["electronics", "clothing", "home", "sports", "books"]
 * - Product model with strict field types
 * - ProductListResponse wrapper
 *
 * IMPORTANT: These types must stay in sync with backend models.
 * Any changes to backend models require updating these types.
 */

/**
 * Product category enum matching backend Literal type.
 *
 * Backend: ProductCategory = Literal["electronics", "clothing", "home", "sports", "books"]
 */
export type ProductCategory = "electronics" | "clothing" | "home" | "sports" | "books";

/**
 * Product model matching backend Pydantic Product model.
 *
 * Backend definition:
 * ```python
 * class Product(BaseModel):
 *     product_id: int = Field(..., gt=0)
 *     product_name: str = Field(..., min_length=1, max_length=200)
 *     product_description: str = Field(..., min_length=1, max_length=1000)
 *     product_price_usd: Decimal = Field(..., gt=0, decimal_places=2)
 *     product_category: ProductCategory
 *     product_in_stock: bool = Field(default=True)
 * ```
 *
 * Note: Decimal from backend is serialized as string in JSON
 */
export interface Product {
  /** Unique product identifier (always positive integer) */
  product_id: number;

  /** Display name of the product (1-200 characters) */
  product_name: string;

  /** Detailed product description (1-1000 characters) */
  product_description: string;

  /** Price in USD as string (Decimal serialized from backend with 2 decimal places) */
  product_price_usd: string;

  /** Product category (one of 5 valid categories) */
  product_category: ProductCategory;

  /** Whether product is currently available for purchase */
  product_in_stock: boolean;
}

/**
 * Product list response matching backend ProductListResponse model.
 *
 * Backend definition:
 * ```python
 * class ProductListResponse(BaseModel):
 *     products: list[Product] = Field(...)
 *     total_count: int = Field(..., ge=0)
 * ```
 */
export interface ProductListResponse {
  /** Array of product objects */
  products: Product[];

  /** Total number of products in response (always >= 0) */
  total_count: number;
}

/**
 * Product filter parameters (for future implementation by students).
 *
 * These match the backend ProductFilterParameters that students will create.
 * Currently not implemented - will be added during the exercise.
 */
export interface ProductFilterParams {
  /** Filter products with price >= this amount */
  minimum_price_usd?: number;

  /** Filter products with price <= this amount */
  maximum_price_usd?: number;

  /** Filter by specific category */
  category?: ProductCategory;

  /** Search keyword in product name/description (case-insensitive) */
  search_keyword?: string;

  /** Sort order for results */
  sort_by?: "price_asc" | "price_desc" | "name_asc" | "name_desc";
}
