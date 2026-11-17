def test_03_validar_titulo_pagina(inventory):
    titulo = inventory.obtener_titulo()

    assert titulo == "Products", \
        f"ERROR: Título esperado: Products, obtenido: {titulo}"


def test_04_productos_visibles(inventory):
    assert inventory.productos_visibles(), \
        "ERROR: La lista de productos no está visible"

    assert len(inventory.obtener_productos()) > 0, \
        "ERROR: No se encontraron productos en el inventario"


def test_05_validar_un_producto(inventory):
    nombres = [p.text for p in inventory.obtener_productos()]

    assert "Sauce Labs Backpack" in nombres, \
        "ERROR: No se encontró Sauce Labs Backpack"


def test_06_validar_interfaz(inventory):
    assert inventory.menu_visible(), \
        "ERROR: El menú hamburguesa no está visible"

    assert inventory.filtro_visible(), \
        "ERROR: El filtro de productos no está visible"


def test_07_agregar_y_quitar_producto(inventory):
    inventory.agregar_primer_producto()

    assert inventory.obtener_contador_carrito() == "1", \
        "ERROR: El contador del carrito no se actualizó al agregar"

    inventory.quitar_primer_producto()

    assert inventory.esperar_carrito_vacio(), \
        "ERROR: El contador del carrito sigue visible después de quitar el producto"