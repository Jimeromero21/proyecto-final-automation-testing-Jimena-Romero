from Page.PageLogin import PageLogin
from Page.PageInventory import PageInventory
from Page.PageCart import PageCart
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.datos import datos_login


def test_08_verificar_contador_carrito(driver, credenciales):

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
            inventory.contador_carrito, "1"
        )
    )

    assert inventory.obtener_contador_carrito() == "1", \
        "ERROR: El contador del carrito no muestra 1"

def test_09_navegar_carrito(driver, credenciales):


    login = PageLogin(driver)

    usuario, password = credenciales

    login.iniciar_sesion(usuario, password)

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventory = PageInventory(driver)

    inventory.agregar_primer_producto()

    inventory.ir_al_carrito()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    cart = PageCart(driver)

    assert cart.obtener_titulo() == "Your Cart", \
        "ERROR: No se ingresó correctamente al carrito"

def test_10_comprobar_producto_en_el_carrito(driver,credenciales):

    login = PageLogin(driver)

    usuario, password = credenciales
    
    login.iniciar_sesion(usuario, password)


    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    inventory = PageInventory(driver)

    inventory.agregar_primer_producto()
    inventory.ir_al_carrito()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    cart = PageCart(driver)

    productos = cart.obtener_nombres_productos()
    nombres = [producto.text for producto in productos]

    assert "Sauce Labs Backpack" in nombres, \
        "ERROR: El producto no aparece en el carrito"
