import pytest
from playwright.sync_api import sync_playwright
import os

# conftest.py
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "getonbr: Descripción del marcador getb"
    )

    # config.option.capture = 'sys'
    

# Crear carpeta para guardar screenshots si no existe
@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

# Fixture para lanzar el navegador
@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Cambia a False si deseas ver el navegador
        context = browser.new_context()  # Crear un nuevo contexto de navegador
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def browser_page(browser_context, request):
    page = browser_context.new_page()

    yield page  # Se pasa la página para que los tests interactúen

    # Toma una captura de pantalla si el test falla
    if request.node.rep_call.failed:
        screenshot_path = os.path.join("screenshots", f"{request.node.name}.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    page.close()

# Hook para capturar fallos y agregar capturas de pantalla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if "browser_page" in item.fixturenames:
            page = item.funcargs["browser_page"]
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            item.extra = getattr(rep, "extra", [])
            if pytest_html:
                item.extra.append(pytest_html.extras.image(screenshot_path))

# Verificación de pytest_html antes de agregar capturas al reporte
@pytest.fixture(autouse=True)
def verify_pytest_html(request):
    global pytest_html
    try:
        pytest_html = request.config.pluginmanager.getplugin("html")
    except AttributeError:
        pytest_html = None

# Hook para configurar el reporte HTML
def pytest_configure(config):
    config.option.htmlpath = "report.html"  # Nombre del archivo de reporte HTML

def pytest_html_report_title(report):
    report.title = "Reporte de pruebas Playwright con pytest"