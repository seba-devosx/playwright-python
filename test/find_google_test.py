import time
import pytest

@pytest.mark.google
def test_google_search(browser_page):
    browser_page.goto("https://www.google.com")
    browser_page.fill("//textarea[contains(@name,'q')]", "Playwright con Python")
    browser_page.press("//textarea[contains(@name,'q')]", "Enter")
    browser_page.wait_for_selector("(//h3[contains(text(),'Installation | Playwright Python')])[1]")
    assert "Playwright" in browser_page.title()

@pytest.mark.portfolio
def test_porfollio(browser_page):
    browser_page.goto("https://portfolio-snowy-six-51.vercel.app/")
    text_habiliti= browser_page.locator("//a[contains(text(),'Habilidades')]").click()
    assert text_habiliti=="Habilidades"
    text_habiliti.click()



   