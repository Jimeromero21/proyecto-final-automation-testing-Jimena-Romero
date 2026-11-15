
from Page.PageLogin import PageLogin
from Page.PageInventory import PageInventory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_01_login(driver):

    driver.get("https://www.saucedemo.com/")

    login = PageLogin(driver)

    login.iniciar_sesion("standard_user", "secret_sauce")

    WebDriverWait (driver, 10).until (
        EC.url_contains ('/inventory.html')
    )

    assert "/inventory.html" in driver.current_url, \
        "ERROR: No redirigio al inventario"


def test_02_validar_titulo_ventana(driver):
    driver.get("https://www.saucedemo.com/")

    login = PageLogin(driver)

    login.iniciar_sesion("standard_user", "secret_sauce")

    page_title = driver.title

    assert page_title == "Swag Labs", \
        f"ERROR: Titulo de ventana esperado: Swag Labs, obtenido {page_title}"


