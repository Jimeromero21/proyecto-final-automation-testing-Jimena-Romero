
import pytest
from Page.PageLogin import PageLogin
from Page.PageInventory import PageInventory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.datos import datos_login



def test_01_login(driver, credenciales):

    login = PageLogin(driver)

    usuario, password = credenciales

    login.iniciar_sesion(usuario, password)

    WebDriverWait (driver, 10).until (
        EC.url_contains ('/inventory.html')
    )

    assert "/inventory.html" in driver.current_url, \
        "ERROR: No redirigio al inventario"


def test_02_validar_titulo_ventana(driver, credenciales):

    usuario, password = credenciales

    login = PageLogin(driver)
    login.iniciar_sesion(usuario, password)

    page_title = driver.title

    assert page_title == "Swag Labs"


