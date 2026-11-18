import csv
from pathlib import Path

import pytest

from page.PageLogin import PageLogin

RUTA_CSV = Path(__file__).resolve().parent.parent / "data" / "usuarios.csv"


def leer_csv_login(ruta_archivo=RUTA_CSV):
    """Lee los usuarios del CSV: (usuario, password, descripcion)."""
    casos = []
    with open(ruta_archivo, mode="r", encoding="utf-8-sig", newline="") as archivo:
        for fila in csv.DictReader(archivo):
            casos.append((
                fila["usuario"].strip(),
                fila["password"].strip(),
                fila["descripcion"].strip(),
            ))
    return casos


CASOS_LOGIN = leer_csv_login()


@pytest.mark.parametrize(
    "usuario, password, descripcion",
    CASOS_LOGIN,
    ids=[caso[2] for caso in CASOS_LOGIN]
)
def test_login_desde_csv(driver, usuario, password, descripcion):
    """Valida que cada usuario del CSV pueda iniciar sesión."""
    login = PageLogin(driver)
    login.iniciar_sesion(usuario, password)

    assert login.login_exitoso(timeout=15), \
        f"ERROR: no se pudo iniciar sesión con {usuario} ({descripcion})"


@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver, credenciales):
    usuario, password = credenciales

    login = PageLogin(driver)
    login.iniciar_sesion(usuario, password)

    assert login.login_exitoso(), "ERROR: el login con usuario válido falló"