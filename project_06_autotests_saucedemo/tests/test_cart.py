def login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

def test_add_to_cart(page):
    login(page)
    page.click("#add-to-cart-sauce-labs-backpack")
    badge = page.text_content(".shopping_cart_badge")
    assert badge == "1"

def test_remove_from_cart(page):
    login(page)
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#remove-sauce-labs-backpack")
    badge = page.locator(".shopping_cart_badge")
    assert badge.count() == 0