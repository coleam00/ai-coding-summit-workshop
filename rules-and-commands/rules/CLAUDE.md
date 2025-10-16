# Product Catalog - AI Development Instructions

## Project Overview

Fullstack e-commerce product catalog: FastAPI backend + React 19 frontend with TypeScript. Service layer (backend), component-based (frontend).

## Core Principles

**TYPE SAFETY IS NON-NEGOTIABLE** - All functions/variables/components MUST have type annotations
**KISS** - Keep It Simple, Stupid
**YAGNI** - You Aren't Gonna Need It

## Architecture

Backend: `api/` (routes) → `services/` (logic) → `models/` (validation) → `data/`
Frontend: `components/` (UI) + `lib/` (api-client, logger) + `types/` (must match backend EXACTLY)

## Naming Conventions

**Backend:**
- Product fields: `product_id`, `product_name`, `product_price_usd` (use `product_` prefix)
- Money: `_usd` suffix + `Decimal` type (NEVER `float`)
- Functions: `filter_products_by_category_and_price_range()` (descriptive)
- Use `snake_case`

**Frontend:**
- Types match backend: `Product`, `ProductListResponse`
- `PascalCase` for components, `camelCase` for variables
- Money is `string`: `product_price_usd: string` (Decimal serialized from backend)

**DO NOT:** Short names (`price`, `min`, `prod`), generic names (`data`, `items`), `float`/`number` for money

## Type Safety

**Backend:**
```python
from decimal import Decimal
from pydantic import BaseModel, Field

class ProductFilterParameters(BaseModel):
    minimum_price_usd: Decimal | None = Field(default=None, ge=0, decimal_places=2)

def filter_products(minimum_price_usd: Decimal | None = None) -> list[Product]:
    """Complete type hints required."""
```

**Frontend:**
```typescript
interface Product {
  product_id: number;
  product_price_usd: string;  // Decimal from backend
}
```

## Logging (Structured JSON)

**Backend:**
```python
from app.core.logging_config import StructuredLogger
logger = StructuredLogger(__name__)

logger.info("filtering_products", filter_category="electronics", total_products=30)
logger.error("validation_failed", error_type="invalid_price_range",
             fix_suggestion="Ensure min_price_usd <= max_price_usd")
```

**Frontend:**
```typescript
import { logger } from "@/lib/logger";

logger.info("fetching_products", { endpoint: "/api/products" });
logger.error("api_call_failed", { error_message: err.message, fix_suggestion: "Check backend" });
```

**Always log:** Operation start (with params), completion (with count), errors (with `fix_suggestion`)
**Never log:** Sensitive data, use string formatting, spam in loops

## Error Handling

**Backend:**
```python
from fastapi import HTTPException
from app.models.error import ErrorResponse

raise HTTPException(
    status_code=400,
    detail=ErrorResponse(
        error_code="invalid_price_range",
        error_message="Minimum price cannot exceed maximum price"
    ).model_dump()
)
```

**Frontend:**
```typescript
import { ApiError } from "@/types/error";

try {
  await fetchProducts();
} catch (err) {
  if (err instanceof ApiError) console.error(err.errorResponse.error_code);
}
```

## Backend Patterns

1. **Service Layer:** Business logic in `services/`, NOT in `api/` routes
2. **Pydantic Everything:** `BaseModel` + `Field()` validation
3. **Query Params:** `filters: ProductFilterParameters = Depends()`
4. **Type Hints:** Every function
5. **Docstrings:** Google-style (Args/Returns/Raises)

## Frontend Patterns (React 19)

1. **React 19:** `use` hook, actions, automatic context selectors
2. **Components:** shadcn/ui (Button, Card, Input, Select, Form), controlled components
3. **State:** `useState` locally, lift when shared
4. **Forms:** React Hook Form + Zod validation, loading/error states
5. **API:** Type-safe client, match backend types EXACTLY, structured logging

## Development

**Start:** Backend: `cd app/backend && uv run python run_api.py` (port 8000)
         Frontend: `cd app/frontend && bun dev` (port 3000)

**Backend:** `uv run ruff check app/`, `uv run pytest tests/ -v`
**Frontend:** `bun run check:fix`, `bun run lint:fix`

## Testing

Backend: Tests mirror source. `uv run pytest tests/ -v`
Frontend: Manual browser testing, check console JSON logs
