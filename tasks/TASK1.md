# [FEAT-1234] Add Product Filtering to Catalog API

## Description

Users need to filter and search products in the catalog API. Currently `GET /api/products` returns all 30 products without filtering capabilities.

## Requirements

Add filtering and search capabilities to `GET /api/products`:

- **Price filtering**: Support minimum and maximum price filters
- **Category filtering**: Allow filtering by product category
- **Keyword search**: Search product names and descriptions
- **Sorting**: Enable sorting by price or name (both directions)

All filters should be optional and work together when combined.

## Acceptance Criteria

- [ ] All filtering tests pass
- [ ] Invalid inputs return appropriate HTTP 400 errors
- [ ] Backwards compatible (no filters = all products)
- [ ] Follows existing code patterns and conventions

## Technical Notes

- Validate query parameters
- Use appropriate types for monetary values
- Log filter operations

## Definition of Done

- All acceptance criteria met
- All Tests passing
  `uv run pytest`
