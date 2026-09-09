# Автотест: Вход на SauceDemo

**Инструменты:** Python, Playwright

**Что тестировалось:** вход на демо-сайт SauceDemo с валидными учетными данными.

**Шаги автотеста:**
1. Открыть браузер
2. Перейти на страницу входа
3. Ввести логин `standard_user`
4. Ввести пароль `secret_sauce`
5. Нажать кнопку "Login"
6. Проверить, что открылась страница с товарами

**Результат:** тест пройден успешно.

**Код:**

```python
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
