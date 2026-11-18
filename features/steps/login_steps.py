from behave import given, when, then

from page.PageLogin import PageLogin


@given('que estoy en la página de login')
def step_pagina_login(context):
    context.login = PageLogin(context.driver)


@given('que inicié sesión con "{usuario}"')
def step_sesion_iniciada(context, usuario):
    context.login = PageLogin(context.driver)
    context.login.iniciar_sesion(usuario, "secret_sauce")
    assert context.login.login_exitoso(timeout=15), \
        f"No se pudo iniciar sesión con {usuario}"


@when('inicio sesión con "{usuario}" y "{password}"')
def step_iniciar_sesion(context, usuario, password):
    context.login.iniciar_sesion(usuario, password)


@then('veo la página de inventario')
def step_ver_inventario(context):
    assert context.login.login_exitoso(timeout=15), \
        "No se redirigió al inventario"


@then('no puedo ingresar al inventario')
def step_no_ingresa(context):
    assert not context.login.login_exitoso(timeout=15), \
        "El login no debería haber sido exitoso"