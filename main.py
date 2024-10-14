

def test_google_search(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("//textarea[contains(@name,'q')]", "Playwright con Python")
    page.press("//textarea[contains(@name,'q')]", "Enter")
    page.wait_for_selector("(//h3[contains(text(),'Installation | Playwright Python')])[1]")
    assert "Playwright" in page.title()

# def run(playwright):
#     # Lanzar el navegador
#     browser = playwright.chromium.launch(headless=True)  # Puedes usar chromium, firefox o webkit
#     page = browser.new_page()

#     # Navegar a Google
#     page.goto("https://www.google.com")
   
#     # Buscar "Playwright con Python"
#     page.fill("//textarea[contains(@name,'q')]", "Playwright con Python")
#     page.press("//textarea[contains(@name,'q')]", "Enter")
#     time.sleep(5)
#     # Esperar a que carguen los resultados
#     page.wait_for_selector('text="Playwright"')

#     # Capturar una captura de pantalla de los resultados
#     page.screenshot(path="search_results.png")

#     # Cerrar el navegador
#     browser.close()

# # Ejecutar Playwright
# with sync_playwright() as playwright:
#     run(playwright)