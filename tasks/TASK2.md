# [FEAT-1235] Add Product Filtering UI to Frontend

## Description

Backend filtering capabilities are now available on `GET /api/products` with query parameters. Users need a frontend interface to interact with these filters and see filtered results.

## Requirements

Build a product filtering interface that connects to the backend filtering API:

- **Price range controls**: Allow users to set minimum and maximum price filters
- **Category selector**: Enable filtering by product category
- **Search input**: Provide keyword search for product names and descriptions
- **Sort controls**: Allow users to sort results by price or name
- **Filter management**: Provide ability to apply and clear filters

The interface should handle loading states, empty results, and validation errors appropriately.

## Acceptance Criteria

- [ ] Price filtering interface works and sends correct query parameters
- [ ] Category selection filters products correctly
- [ ] Search input filters products by keyword
- [ ] Sort options reorder products as expected
- [ ] Multiple filters work together (combined filtering)
- [ ] Clear filters returns to showing all products
- [ ] Validation errors are displayed to users
- [ ] Empty state shown when no products match filters
- [ ] Loading state shown during filter operations
- [ ] All filter interactions logged to console (structured JSON)

## Technical Notes

- Update API client to accept filter parameters
- Build query string from filter values
- Use React Hook Form and Zod for form validation
- Follow existing logging patterns (structured JSON)
- Use existing shadcn components where possible

## Definition of Done

- All acceptance criteria met
- Backend API called with correct query parameters
- Follows existing code patterns and conventions
- Manual testing checklist completed
