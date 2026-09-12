def test_successful_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert "inventory" in page.url

def test_wrong_password(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    error = page.text_content("h3[data-test='error']")
    assert "Username and password do not match" in error

def test_empty_fields(page):
    page.goto("https://www.saucedemo.com/")
    page.click("#login-button")
    error = page.text_content("h3[data-test='error']")
    assert "Username is required" in error