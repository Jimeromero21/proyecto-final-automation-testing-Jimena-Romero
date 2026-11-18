import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import BASE_URL
from data.datos import datos_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.datos import datos_login
from Page.PageLogin import PageLogin
from Page.PageInventory import PageInventory



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.get(BASE_URL)

    yield driver

    driver.quit()

@pytest.fixture(params=datos_login)
def credenciales(request):
    return request.param

@pytest.fixture
def inventory(driver, credenciales):
    usuario, password = credenciales
    PageLogin(driver).iniciar_sesion(usuario, password)
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    return PageInventory(driver)