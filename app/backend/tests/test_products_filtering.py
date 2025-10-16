"""
Tests for product filtering functionality.

These tests are currently STUBS - they will fail until you implement
the filtering functionality. Your goal is to make all these tests pass!

Run these tests with:
    pytest tests/test_products_filtering.py -v
"""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_filter_products_by_minimum_price(test_client: TestClient) -> None:
    """
    Test filtering products by minimum price.

    When min_price_usd=100 is provided, only products costing $100 or more
    should be returned.

    Expected: Should return products like "Wireless Earbuds Pro" ($149.99),
    "Smart Robot Vacuum" ($299.99), "Adjustable Dumbbell Set" ($499.99), etc.
    """
    response = test_client.get("/api/products?min_price_usd=100")
    data = response.json()

    assert response.status_code == 200
    assert all(
        float(product["product_price_usd"]) >= 100
        for product in data["products"]
    )


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_filter_products_by_maximum_price(test_client: TestClient) -> None:
    """
    Test filtering products by maximum price.

    When max_price_usd=30 is provided, only products costing $30 or less
    should be returned.

    Expected: Should return products like "Smart LED Light Bulb" ($19.99),
    "Classic Cotton T-Shirt" ($24.99), "Merino Wool Beanie" ($29.99), etc.
    """
    response = test_client.get("/api/products?max_price_usd=30")
    data = response.json()

    assert response.status_code == 200
    assert all(
        float(product["product_price_usd"]) <= 30
        for product in data["products"]
    )


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_filter_products_by_price_range(test_client: TestClient) -> None:
    """
    Test filtering products by both minimum and maximum price.

    When min_price_usd=25 and max_price_usd=50 are provided, only products
    in that price range should be returned.

    Expected: Should return products like "Wireless Bluetooth Mouse" ($29.99),
    "USB-C Hub 7-in-1" ($45.99), "Ceramic Non-Stick Frying Pan" ($49.99), etc.
    """
    response = test_client.get("/api/products?min_price_usd=25&max_price_usd=50")
    data = response.json()

    assert response.status_code == 200
    assert all(
        25 <= float(product["product_price_usd"]) <= 50
        for product in data["products"]
    )


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_filter_products_by_category(test_client: TestClient) -> None:
    """
    Test filtering products by category.

    When category=electronics is provided, only electronics products
    should be returned.

    Expected: Should return 8 electronics products (IDs 1-8).
    """
    response = test_client.get("/api/products?category=electronics")
    data = response.json()

    assert response.status_code == 200
    assert all(
        product["product_category"] == "electronics"
        for product in data["products"]
    )
    # We have 8 electronics products in seed data
    assert len(data["products"]) == 8


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_search_products_by_keyword(test_client: TestClient) -> None:
    """
    Test searching products by keyword.

    When search_keyword=wireless is provided, only products with "wireless"
    in their name or description should be returned (case-insensitive).

    Expected: Should return "Wireless Bluetooth Mouse", "Wireless Earbuds Pro",
    "Wireless Charger Stand", etc.
    """
    response = test_client.get("/api/products?search_keyword=wireless")
    data = response.json()

    assert response.status_code == 200
    # All returned products should have "wireless" in name or description
    for product in data["products"]:
        name_lower = product["product_name"].lower()
        desc_lower = product["product_description"].lower()
        assert "wireless" in name_lower or "wireless" in desc_lower


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_filter_with_multiple_parameters(test_client: TestClient) -> None:
    """
    Test filtering with multiple parameters combined.

    When category=electronics AND max_price_usd=50 are provided, only
    electronics products costing $50 or less should be returned.

    Expected: Should return products like "Wireless Bluetooth Mouse" ($29.99),
    "USB-C Hub 7-in-1" ($45.99), "Smart LED Light Bulb" ($19.99), etc.
    """
    response = test_client.get("/api/products?category=electronics&max_price_usd=50")
    data = response.json()

    assert response.status_code == 200
    assert all(
        product["product_category"] == "electronics" and
        float(product["product_price_usd"]) <= 50
        for product in data["products"]
    )


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_invalid_price_range_returns_400(test_client: TestClient) -> None:
    """
    Test that invalid price range (min > max) returns HTTP 400 error.

    When min_price_usd is greater than max_price_usd, the API should
    return a 400 Bad Request error with a clear error message.

    Expected error response:
    {
        "error_code": "invalid_price_range",
        "error_message": "Minimum price cannot exceed maximum price",
        "error_details": {...},
        "timestamp_utc": "..."
    }
    """
    response = test_client.get("/api/products?min_price_usd=100&max_price_usd=50")
    data = response.json()

    assert response.status_code == 400
    assert "error_code" in data
    assert data["error_code"] == "invalid_price_range"


@pytest.mark.skip(reason="Not implemented yet - this is your exercise!")
def test_no_filters_returns_all_products(test_client: TestClient) -> None:
    """
    Test that when no filters are provided, all products are returned.

    This ensures that filtering is optional and the default behavior
    (no parameters) still works correctly.

    Expected: Should return all 30 products.
    """
    response = test_client.get("/api/products")
    data = response.json()

    assert response.status_code == 200
    assert data["total_count"] == 30
    assert len(data["products"]) == 30
