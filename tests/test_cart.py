import pytest
from playwright.sync_api import sync_playwright

# 使用 pytest fixture 启动和关闭浏览器
@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # 改成 False 可以看到真实浏览器
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_add_to_cart(browser_context):
    page = browser_context

    # 1. 打开 Sauce Demo 登录页
    page.goto("https://www.saucedemo.com/")

    # 2. 登录
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # 3. 验证登录成功（检查是否进入商品页）
    assert "inventory" in page.url

    # 4. 点击第一个商品 "Add to cart"
    page.click("button[data-test='add-to-cart-sauce-labs-backpack']")

    # 5. 去购物车页面
    page.click(".shopping_cart_link")

    # 6. 验证购物车里有商品
    assert page.is_visible(".inventory_item_name")

    # 7. 再次确认购物车有 "Sauce Labs Backpack"
    product_name = page.inner_text(".inventory_item_name")
    assert product_name == "Sauce Labs Backpack"
