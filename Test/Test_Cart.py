from page.PageCart import PageCart


def test_08_verificar_contador_carrito(inventory):
    inventory.agregar_primer_producto()

    assert inventory.obtener_contador_carrito() == "1", \
        "ERROR: El contador del carrito no muestra 1"


def test_09_navegar_carrito(driver, inventory):
    inventory.agregar_primer_producto()
    inventory.ir_al_carrito()

    cart = PageCart(driver)

    assert cart.obtener_titulo() == "Your Cart", \
        "ERROR: No se ingresó correctamente al carrito"


def test_10_comprobar_producto_en_el_carrito(driver, inventory):
    nombre_agregado = inventory.agregar_primer_producto()
    inventory.ir_al_carrito()

    cart = PageCart(driver)

    assert nombre_agregado in cart.obtener_nombres_productos(), \
        f"ERROR: {nombre_agregado} no aparece en el carrito"


def test_11_boton_checkout_visible(driver, inventory):
    inventory.agregar_primer_producto()
    inventory.ir_al_carrito()

    cart = PageCart(driver)

    assert cart.checkout_visible(), \
        "ERROR: El botón Checkout no está visible en el carrito"


def test_12_continuar_comprando(driver, inventory):
    inventory.agregar_primer_producto()
    inventory.ir_al_carrito()

    cart = PageCart(driver)
    cart.continuar_comprando()

    assert "/inventory.html" in driver.current_url, \
        "ERROR: Continue Shopping no volvió al inventario"