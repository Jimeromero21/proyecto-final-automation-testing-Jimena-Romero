from Page.PageLogin import PageLogin
from Page.PageInventory import PageInventory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.datos import datos_login



def test_03_validar_titulo_pagina(driver, credenciales):

    login = PageLogin(driver)


    usuario, password = credenciales
    
    login.iniciar_sesion(usuario, password)

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventory = PageInventory(driver)

    titulo = inventory.obtener_titulo()

    assert titulo == "Products", \
        f"ERROR: Titulo esperado: Products, obtenido: {titulo}"

def test_04_productos_visibles(driver, credenciales):


    login = PageLogin(driver)
    usuario, password = credenciales
    
    login.iniciar_sesion(usuario, password)

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventory = PageInventory(driver)

    assert inventory.productos_visibles(), \
        "ERROR: La lista de productos no está visible"

    productos = inventory.obtener_productos()

    assert len(productos) > 0, \
        "ERROR: No se encontraron productos en el inventario"

def test_05_validar_un_producto(driver, credenciales):

    login = PageLogin(driver)
    usuario, password = credenciales
    
    login.iniciar_sesion(usuario, password)
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventory = PageInventory(driver)

    productos = inventory.obtener_productos()

    nombres = [producto.text for producto in productos]

    assert "Sauce Labs Backpack" in nombres, \
        "ERROR: No se encontró Sauce Labs Backpack"
def test_06_validar_interfaz(driver, credenciales):


    login = PageLogin(driver)
    usuario, password = credenciales
    
    login.iniciar_sesion(usuario, password)
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventory = PageInventory(driver)

    assert inventory.menu_visible(), \
        "ERROR: El menú hamburguesa no está visible"

    assert inventory.filtro_visible(), \
        "ERROR: El filtro de productos no está visible"
    
def test_07_crear_item(driver, credenciales):

    login = PageLogin(driver)

    usuario, password = credenciales
        
    login.iniciar_sesion(usuario, password)

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventory = PageInventory(driver)

    inventory.agregar_primer_producto()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"), "1"
        )
    )

    assert inventory.obtener_contador_carrito() == "1", \
        "ERROR: El contador del carrito no se actualizó"
