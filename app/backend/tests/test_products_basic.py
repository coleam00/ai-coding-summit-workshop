"""
Basic tests for the products API (before filtering is added).

These tests verify the basic GET /api/products endpoint works correctly.
They demonstrate the testing pattern you should follow when implementing
the filtering functionality.
"""

from fastapi.testclient import TestClient


def test_get_all_products_returns_200(test_client: TestClient) -> None:
    """
    Test that GET /api/products returns HTTP 200 status code.

    This is the most basic test - just checking the endpoint is reachable
    and returns a successful response.
    """
    response = test_client.get("/api/products")

    assert response.status_code == 200


def test_get_all_products_returns_correct_structure(test_client: TestClient) -> None:
    """
    Test that GET /api/products returns the expected JSON structure.

    The response should have:
    - "products": list of product objects
    - "total_count": integer count of products
    """
    response = test_client.get("/api/products")
    data = response.json()

    # Verify response structure
    assert "products" in data
    assert "total_count" in data

    # Verify types
    assert isinstance(data["products"], list)
    assert isinstance(data["total_count"], int)


def test_get_all_products_returns_30_products(test_client: TestClient) -> None:
    """
    Test that GET /api/products returns all 30 seed products.

    Since we have 30 products in our seed data, we should get all of them
    when no filters are applied.
    """
    response = test_client.get("/api/products")
    data = response.json()

    assert data["total_count"] == 30
    assert len(data["products"]) == 30


def test_product_objects_have_required_fields(test_client: TestClient) -> None:
    """
    Test that each product object contains all required fields.

    Every product should have:
    - product_id
    - product_name
    - product_description
    - product_price_usd
    - product_category
    - product_in_stock
    """
    response = test_client.get("/api/products")
    data = response.json()

    products = data["products"]
    assert len(products) > 0  # Make sure we have products to test

    # Check first product has all fields (spot check)
    first_product = products[0]
    required_fields = [
        "product_id",
        "product_name",
        "product_description",
        "product_price_usd",
        "product_category",
        "product_in_stock"
    ]

    for field in required_fields:
        assert field in first_product


def test_health_check_endpoint(test_client: TestClient) -> None:
    """
    Test that the /health endpoint works correctly.

    This is a simple sanity check to ensure the app is running.
    """
    response = test_client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
