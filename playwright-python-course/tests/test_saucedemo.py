import pytest
from playwright.sync_api import Page, expect
# E-commerce Web Automation
# Test saytı: SauceDemo
# Login — valid credentials
# Login — invalid credentials
# Login — empty username/password
# Products səhifəsinin açılması
# Məhsul sayının yoxlanılması
# Məhsulun səbətə əlavə edilməsi
# Cart səhifəsində məhsulun yoxlanılması
# Məhsulun səbətdən silinməsi
# Checkout prosesinin tamamlanması
# Testlərin Pytest parametrization ilə yazılması
# Texniki tələblər:
# Python + Playwright + Pytest
# Fixture istifadəsi
# Playwright assertions
# Testlərin ayrı-ayrı funksiyalarda yazılması
# Screenshot və debugging

@pytest.fixture
def logged_in(page:Page):
    page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    return page


@pytest.mark.parametrize(
    "username,password,result",
    [
        ("standard_user","secret_sauce","Success"),
        ("invalid","invalid","Epic sadface: Username and password do not match any user in this service"),
        ("","secret_sauce","Epic sadface: Username is required"),
        ("standard_user","","Epic sadface: Password is required"),
    ]
)
def test_login(page:Page,username,password,result):
    page.goto("https://www.saucedemo.com/?utm_source=chatgpt.com")
    if username:
        page.locator("#user-name").fill(username)
    if password:
        page.locator("#password").fill(password)
    page.locator("#login-button").click()
    if result=="Success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        error_e =page.locator("[data-test='error']")
        expect(error_e).to_be_visible()

def test_products(logged_in:Page):
    expect(logged_in).to_have_url("https://www.saucedemo.com/inventory.html")
    Count = logged_in.locator(".inventory_item_name")
    expect(Count).to_have_count(6)

    logged_in.screenshot(path="screenshot.png")


def test_add_delete(logged_in:Page):
    expect(logged_in).to_have_url("https://www.saucedemo.com/inventory.html")

    logged_in.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    logged_in.locator("[data-test='shopping-cart-link']").click()
    item_name = logged_in.locator(".inventory_item_name")
    expect(item_name).to_have_text("Sauce Labs Bolt T-Shirt")
    logged_in.locator("#remove-sauce-labs-bolt-t-shirt").click()

    logged_in.screenshot(path="screenshot.png")

def test_checkout(logged_in:Page):
    logged_in.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    logged_in.locator("[data-test='shopping-cart-link']").click()
    logged_in.locator("#checkout").click()
    logged_in.locator("#first-name").fill("Aytan")
    logged_in.locator("#last-name").fill("Yahyayeva")
    logged_in.locator("#postal-code").fill("5005")
    logged_in.locator("#continue").click()
    logged_in.locator("#finish").click()
    last_text=logged_in.locator("[data-test='complete-header']")
    expect(last_text).to_have_text("Thank you for your order!")

    logged_in.screenshot(path="screenshot.png")
























