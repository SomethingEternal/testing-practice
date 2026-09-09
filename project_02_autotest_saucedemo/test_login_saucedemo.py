from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.wait_for_timeout(2000)
    
    if "inventory" in page.url:
        print("✅ Вход выполнен!")
    else:
        print("❌ Что-то пошло не так")
    
    input("Нажми Enter, чтобы закрыть браузер...")
    browser.close()