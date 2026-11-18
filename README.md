# Automatización de pruebas: SauceDemo (UI) y JSONPlaceholder (API)

Proyecto de automatización de pruebas con **Python**, **Selenium** y **Pytest**.
Incluye dos partes:

- **Pruebas de interfaz (UI)** sobre https://www.saucedemo.com, con el patrón **Page Object Model (POM)**.
- **Pruebas de API** sobre https://jsonplaceholder.typicode.com, con la librería `requests`.

**Autora:** Jimena Romero

---

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3.10+ | Lenguaje |
| Selenium | Automatización del navegador |
| Pytest | Ejecución de tests y fixtures |
| pytest-html | Reporte HTML |
| Requests | Consumo de la API |

## Estructura del proyecto

```
.
├── Page/                    Page Objects (UI)
│   ├── PageLogin.py
│   ├── PageInventory.py
│   └── PageCart.py
├── Test/                    Tests de UI
│   ├── test_Login.py
│   ├── Test_inventory.py
│   ├── Test_Cart.py
│   ├── test_logincsv.py     Login con datos desde CSV
│   └── test_loginjson.py    Login con datos desde JSON
├── api/
│   ├── __init__.py
│   └── client.py            Cliente de la API (requests.Session)
├── tests_api/               Tests de API
│   ├── conftest.py          Fixture "client"
│   ├── test_posts.py
│   ├── test_posts_escritura.py
│   ├── test_usuarios.py
│   └── test_todos.py
├── data/                    Datos de prueba
│   ├── usuarios.csv
│   └── usuarios.json
├── reports/                 Reporte HTML generado por pytest
├── config.py                URLs y configuración compartida
├── conftest.py              Fixtures de UI (driver, credenciales, inventory)
├── pytest.ini               Configuración de pytest
└── requirements.txt         Dependencias
```

## Requisitos

- Python 3.10 o superior
- Google Chrome instalado
- Conexión a internet (los sitios probados son públicos)

Selenium descarga automáticamente el driver de Chrome, no hace falta instalarlo a mano.

## Instalación

```powershell
git clone https://github.com/Jimeromero21/Entrega-automation-testing-Jimena-Romero.git
cd Entrega-automation-testing-Jimena-Romero
python -m pip install -r requirements.txt
```

## Ejecución

> Se usa `python -m pytest` en lugar de `pytest` porque en algunos equipos
> Windows bloquea el ejecutable `pytest.exe`.

**Todos los tests**

```powershell
python -m pytest -v
```

**Solo pruebas de UI**

```powershell
python -m pytest Test -v
```

**Solo pruebas de API**

```powershell
python -m pytest tests_api -v
```

**Un archivo**

```powershell
python -m pytest Test/test_logincsv.py -v
```

**Un test puntual**

```powershell
python -m pytest Test/Test_inventory.py::test_03_validar_titulo_pagina -v
```

**Buscar por nombre**

```powershell
python -m pytest -k login -v
```

**Solo pruebas de humo (smoke)**

```powershell
python -m pytest -m smoke -v
```

**Ver qué tests hay sin ejecutarlos**

```powershell
python -m pytest --collect-only -q
```

## Reporte

Al terminar cada ejecución se genera un reporte HTML en `reports/reporte.html`.
Se abre con cualquier navegador.

---

## Pruebas de UI (SauceDemo)

### Patrón Page Object Model

Cada pantalla tiene su clase en `Page/`, con los localizadores y las acciones.
Los tests no usan localizadores directamente: llaman a los métodos del Page Object.

- `PageLogin`: iniciar sesión, validar si el login fue exitoso.
- `PageInventory`: título, lista de productos, menú, filtro, agregar y quitar productos, contador del carrito.
- `PageCart`: título, productos del carrito, botón Checkout, continuar comprando.

### Fixtures (`conftest.py`)

| Fixture | Qué hace |
|---|---|
| `driver` | Abre y cierra el navegador en cada test |
| `credenciales` | Entrega `(usuario, password)`; el test se ejecuta una vez por cada usuario definido |
| `inventory` | Inicia sesión, espera el inventario y devuelve un `PageInventory` listo para usar |

### Casos cubiertos

| Área | Casos |
|---|---|
| Login | Inicio de sesión exitoso, título de la ventana |
| Login con datos externos | Usuarios leídos desde `usuarios.csv` y `usuarios.json` |
| Inventario | Título de la página, productos visibles, producto esperado, menú y filtro, agregar y quitar un producto |
| Carrito | Contador, navegación al carrito, producto agregado presente, botón Checkout, continuar comprando |

### Datos de prueba

Los usuarios se definen fuera del código, en `data/`:

`data/usuarios.csv`

```
usuario,password,descripcion
standard_user,secret_sauce,Usuario estándar válido
performance_glitch_user,secret_sauce,Usuario con lentitud simulada
```

`data/usuarios.json`

```json
[
    {"usuario": "standard_user", "password": "secret_sauce"},
    {"usuario": "performance_glitch_user", "password": "secret_sauce"}
]
```

Para probar otro usuario alcanza con agregar una fila al archivo; el test se repite automáticamente por cada una.

---

## Pruebas de API (JSONPlaceholder)

El cliente `JsonPlaceholderClient` (`api/client.py`) usa una `requests.Session` y expone un método por cada operación. Los tests lo reciben mediante la fixture `client` y deciden qué validar (código de estado, cuerpo, headers).

### Casos cubiertos

| Archivo | Qué prueba |
|---|---|
| `test_posts.py` | Filtro por usuario, error 404 en post inexistente, comentarios de un post, tipo de contenido JSON |
| `test_posts_escritura.py` | POST (crear), PUT (reemplazar), PATCH (modificar un campo), DELETE |
| `test_usuarios.py` | Listado, campos básicos (parametrizado), posts de un usuario, usuario inexistente |
| `test_todos.py` | Filtros por estado y por usuario |


---

## Configuración

Las URLs viven en `config.py`:

```python
BASE_URL = "https://www.saucedemo.com/"          # UI
API_BASE_URL = "https://jsonplaceholder.typicode.com"  # API
API_TIMEOUT = 10
```

## Problemas comunes

| Problema | Solución |
|---|---|
| `pytest.exe` bloqueado por una política de Windows | Usar `python -m pytest` |
| `ModuleNotFoundError: No module named 'api'` | Verificar que exista `api/__init__.py` y ejecutar desde la carpeta raíz del proyecto |
| Pytest no detecta un archivo de tests | El nombre debe empezar con `test_` (no `tests_`) |
| Fallo por tiempo de espera con `performance_glitch_user` | Es un usuario lento a propósito; aumentar el timeout de la espera |

## Pruebas BDD (Behave)

Los escenarios están escritos en Gherkin (español) en `features/` y reutilizan
los Page Objects del proyecto.

python -m behave                      # todos los escenarios
python -m behave --tags=@smoke        # solo humo
python -m behave --tags=@regression   # solo regresión

Estructura: `features/*.feature` (escenarios), `features/steps/` (pasos) y
`features/environment.py` (apertura y cierre del navegador).