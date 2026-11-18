
from page.PageLogin import PageLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_login(driver, credenciales):
    usuario, password = credenciales

    PageLogin(driver).iniciar_sesion(usuario, password)

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    assert "/inventory.html" in driver.current_url, \
        "ERROR: No redirigió al inventario"


def test_02_validar_titulo_ventana(driver, inventory):
    assert driver.title == "Swag Labs", \
        f"ERROR: Título esperado: Swag Labs, obtenido: {driver.title}"