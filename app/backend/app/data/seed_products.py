"""
Sample product data for the e-commerce catalog.

This module contains 30 diverse products across all categories to provide
realistic test data for the API. Prices range from $5.99 to $499.99.
"""

from decimal import Decimal

from app.models.product import Product


def get_seed_products() -> list[Product]:
    """
    Return a list of 30 sample products for the catalog.

    The products are diverse across all five categories (electronics, clothing,
    home, sports, books) with a range of prices. Some products are marked as
    out of stock to test filtering edge cases.

    Returns:
        List of Product objects ready to use in the API

    Example:
        >>> products = get_seed_products()
        >>> len(products)
        30
        >>> products[0].product_category
        'electronics'
    """
    return [
        # Electronics (8 products)
        Product(
            product_id=1,
            product_name="Wireless Bluetooth Mouse",
            product_description="Ergonomic wireless mouse with 2.4GHz USB receiver and long-lasting battery life",
            product_price_usd=Decimal("29.99"),
            product_category="electronics",
            product_in_stock=True,
        ),
        Product(
            product_id=2,
            product_name="Mechanical Gaming Keyboard",
            product_description="RGB backlit mechanical keyboard with blue switches and programmable macros",
            product_price_usd=Decimal("89.99"),
            product_category="electronics",
            product_in_stock=True,
        ),
        Product(
            product_id=3,
            product_name="USB-C Hub 7-in-1",
            product_description="Multi-port USB-C hub with HDMI, SD card reader, and 100W power delivery",
            product_price_usd=Decimal("45.99"),
            product_category="electronics",
            product_in_stock=True,
        ),
        Product(
            product_id=4,
            product_name="Wireless Earbuds Pro",
            product_description="Active noise cancelling wireless earbuds with 30-hour battery life and charging case",
            product_price_usd=Decimal("149.99"),
            product_category="electronics",
            product_in_stock=False,
        ),
        Product(
            product_id=5,
            product_name="4K Webcam",
            product_description="Ultra HD 4K webcam with autofocus, ring light, and dual microphones",
            product_price_usd=Decimal("119.99"),
            product_category="electronics",
            product_in_stock=True,
        ),
        Product(
            product_id=6,
            product_name="Portable SSD 1TB",
            product_description="Ultra-fast portable solid state drive with USB 3.2 Gen 2 speeds up to 1050MB/s",
            product_price_usd=Decimal("129.99"),
            product_category="electronics",
            product_in_stock=True,
        ),
        Product(
            product_id=7,
            product_name="Smart LED Light Bulb",
            product_description="WiFi-enabled color-changing LED bulb compatible with Alexa and Google Home",
            product_price_usd=Decimal("19.99"),
            product_category="electronics",
            product_in_stock=True,
        ),
        Product(
            product_id=8,
            product_name="Wireless Charger Stand",
            product_description="15W fast wireless charging stand with adjustable viewing angle for smartphones",
            product_price_usd=Decimal("34.99"),
            product_category="electronics",
            product_in_stock=True,
        ),
        # Clothing (7 products)
        Product(
            product_id=9,
            product_name="Classic Cotton T-Shirt",
            product_description="100% organic cotton crew neck t-shirt available in multiple colors",
            product_price_usd=Decimal("24.99"),
            product_category="clothing",
            product_in_stock=True,
        ),
        Product(
            product_id=10,
            product_name="Slim Fit Denim Jeans",
            product_description="Stretch denim jeans with modern slim fit and classic 5-pocket styling",
            product_price_usd=Decimal("59.99"),
            product_category="clothing",
            product_in_stock=True,
        ),
        Product(
            product_id=11,
            product_name="Hooded Zip Sweatshirt",
            product_description="Comfortable fleece-lined hoodie with full zip and kangaroo pockets",
            product_price_usd=Decimal("44.99"),
            product_category="clothing",
            product_in_stock=True,
        ),
        Product(
            product_id=12,
            product_name="Running Jacket Windbreaker",
            product_description="Lightweight water-resistant windbreaker with reflective details for running",
            product_price_usd=Decimal("69.99"),
            product_category="clothing",
            product_in_stock=False,
        ),
        Product(
            product_id=13,
            product_name="Merino Wool Beanie",
            product_description="Soft merino wool winter beanie hat with fold-over cuff design",
            product_price_usd=Decimal("29.99"),
            product_category="clothing",
            product_in_stock=True,
        ),
        Product(
            product_id=14,
            product_name="Canvas Sneakers",
            product_description="Classic low-top canvas sneakers with rubber sole and cushioned insole",
            product_price_usd=Decimal("54.99"),
            product_category="clothing",
            product_in_stock=True,
        ),
        Product(
            product_id=15,
            product_name="Leather Crossbody Bag",
            product_description="Genuine leather crossbody bag with adjustable strap and multiple compartments",
            product_price_usd=Decimal("89.99"),
            product_category="clothing",
            product_in_stock=True,
        ),
        # Home (7 products)
        Product(
            product_id=16,
            product_name="Stainless Steel French Press",
            product_description="34oz double-wall insulated French press coffee maker with heat-resistant handle",
            product_price_usd=Decimal("39.99"),
            product_category="home",
            product_in_stock=True,
        ),
        Product(
            product_id=17,
            product_name="Ceramic Non-Stick Frying Pan",
            product_description="10-inch ceramic-coated frying pan with ergonomic handle and even heat distribution",
            product_price_usd=Decimal("49.99"),
            product_category="home",
            product_in_stock=True,
        ),
        Product(
            product_id=18,
            product_name="Memory Foam Pillow Set",
            product_description="Set of 2 bamboo-covered memory foam pillows with adjustable fill for custom comfort",
            product_price_usd=Decimal("79.99"),
            product_category="home",
            product_in_stock=True,
        ),
        Product(
            product_id=19,
            product_name="Smart Robot Vacuum",
            product_description="App-controlled robot vacuum with auto-recharge and scheduled cleaning features",
            product_price_usd=Decimal("299.99"),
            product_category="home",
            product_in_stock=False,
        ),
        Product(
            product_id=20,
            product_name="Bamboo Cutting Board Set",
            product_description="Set of 3 bamboo cutting boards with juice grooves and non-slip feet",
            product_price_usd=Decimal("34.99"),
            product_category="home",
            product_in_stock=True,
        ),
        Product(
            product_id=21,
            product_name="Aromatherapy Essential Oil Diffuser",
            product_description="Ultrasonic essential oil diffuser with 7 LED light colors and auto shut-off",
            product_price_usd=Decimal("29.99"),
            product_category="home",
            product_in_stock=True,
        ),
        Product(
            product_id=22,
            product_name="Weighted Blanket 15lbs",
            product_description="Premium weighted blanket with glass beads and soft breathable cotton cover",
            product_price_usd=Decimal("89.99"),
            product_category="home",
            product_in_stock=True,
        ),
        # Sports (5 products)
        Product(
            product_id=23,
            product_name="Yoga Mat with Carrying Strap",
            product_description="6mm thick non-slip yoga mat with alignment marks and free carrying strap",
            product_price_usd=Decimal("39.99"),
            product_category="sports",
            product_in_stock=True,
        ),
        Product(
            product_id=24,
            product_name="Adjustable Dumbbell Set",
            product_description="Pair of adjustable dumbbells from 5-52.5 lbs with quick-change dial system",
            product_price_usd=Decimal("499.99"),
            product_category="sports",
            product_in_stock=True,
        ),
        Product(
            product_id=25,
            product_name="Resistance Bands Set",
            product_description="Set of 5 resistance bands with handles, door anchor, and carrying bag",
            product_price_usd=Decimal("24.99"),
            product_category="sports",
            product_in_stock=True,
        ),
        Product(
            product_id=26,
            product_name="Foam Roller for Muscle Recovery",
            product_description="High-density foam roller for deep tissue massage and muscle recovery",
            product_price_usd=Decimal("29.99"),
            product_category="sports",
            product_in_stock=True,
        ),
        Product(
            product_id=27,
            product_name="Sports Water Bottle 32oz",
            product_description="Insulated stainless steel water bottle keeps drinks cold for 24 hours",
            product_price_usd=Decimal("34.99"),
            product_category="sports",
            product_in_stock=False,
        ),
        # Books (3 products)
        Product(
            product_id=28,
            product_name="The Pragmatic Programmer",
            product_description="Classic software development book with timeless programming wisdom and best practices",
            product_price_usd=Decimal("44.99"),
            product_category="books",
            product_in_stock=True,
        ),
        Product(
            product_id=29,
            product_name="Atomic Habits",
            product_description="Science-backed strategies for building good habits and breaking bad ones",
            product_price_usd=Decimal("16.99"),
            product_category="books",
            product_in_stock=True,
        ),
        Product(
            product_id=30,
            product_name="The Design of Everyday Things",
            product_description="Foundational book on user-centered design and human-computer interaction",
            product_price_usd=Decimal("24.99"),
            product_category="books",
            product_in_stock=True,
        ),
    ]
