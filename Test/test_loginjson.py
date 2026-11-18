import json
from pathlib import Path

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.PageLogin import PageLogin

RUTA_JSON = Path(__file__).resolve().parents[1] / "data" / "usuarios.json"


def leer_datos_json():
    datos = []
    with open(RUTA_JSON, mode="r", encoding="utf-8-sig") as archivo:
        filas = json.load(archivo)

    for fila in filas:
        datos.append((fila["usuario"], fila["password"]))

    return datos


DATOS_JSON = leer_datos_json()


@pytest.mark.parametrize(
    "usuario, password",
    DATOS_JSON,
    ids=[usuario for usuario, _ in DATOS_JSON]
)
def test_login_desde_json(driver, usuario, password):
    login = PageLogin(driver)
    login.iniciar_sesion(usuario, password)

    WebDriverWait(driver, 15).until(EC.url_contains("/inventory.html"))

    assert "/inventory.html" in driver.current_url, \
        f"ERROR: no se pudo iniciar sesión con {usuario}"