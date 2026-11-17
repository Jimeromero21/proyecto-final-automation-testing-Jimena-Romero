import csv
from pathlib import Path

RUTA_USUARIOS = Path(__file__).resolve().parent / "usuarios.csv"


def leer_csv_login(ruta_archivo=RUTA_USUARIOS):
    casos = []
    with open(ruta_archivo, mode="r", encoding="utf-8-sig", newline="") as archivo:
        for fila in csv.DictReader(archivo):
            casos.append((
                fila["usuario"].strip(),
                fila["password"].strip(),
                fila["descripcion"].strip(),
            ))
    return casos


datos_login = [(u, p) for u, p, _ in leer_csv_login()]