import pytest
from playwright.sync_api import sync_playwright

# Use a pytest fixture to start and close the browser


@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=True)  # Change to False to see the real browser
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_add_to_cart(browser_context):
    page = browser_context

    # 1. Open Sauce Demo login page
    page.goto("https://www.saucedemo.com/")

    # 2. Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # 3. Verify login success (check if navigated to inventory page)
    assert "inventory" in page.url

    # 4. Click the first product "Add to cart"
    page.click("button[data-test='add-to-cart-sauce-labs-backpack']")

    # 5. Go to the cart page
    page.click(".shopping_cart_link")

    # 6. Verify there are items in the cart
    assert page.is_visible(".inventory_item_name")

    # 7. Verify the cart contains "Sauce Labs Backpack"
    product_name = page.inner_text(".inventory_item_name")
    assert product_name == "Sauce Labs Backpack"
