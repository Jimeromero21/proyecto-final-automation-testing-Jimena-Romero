import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import BASE_URL
from data.datos import datos_login


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