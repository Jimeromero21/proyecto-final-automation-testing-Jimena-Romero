from behave import when, then

from page.PageInventory import PageInventory
from page.PageCart import PageCart


@when('agrego el primer producto')
def step_agregar_producto(context):
    context.inventory = PageInventory(context.driver)
    context.nombre_agregado = context.inventory.agregar_primer_producto()


@when('voy al carrito')
def step_ir_al_carrito(context):
    context.inventory.ir_al_carrito()
    context.cart = PageCart(context.driver)


@then('el contador del carrito muestra "{cantidad}"')
def step_contador(context, cantidad):
    assert context.inventory.obtener_contador_carrito() == cantidad


@then('el producto agregado está en el carrito')
def step_producto_en_carrito(context):
    assert context.nombre_agregado in context.cart.obtener_nombres_productos()