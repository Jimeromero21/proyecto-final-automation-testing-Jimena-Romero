def test_crear_post(client):
    datos = {"title": "Mi post de prueba", "body": "Contenido", "userId": 1}

    respuesta = client.crear_post(datos)

    assert respuesta.status_code == 201
    creado = respuesta.json()
    assert creado["title"] == datos["title"]
    assert creado["userId"] == 1
    assert isinstance(creado["id"], int)


def test_reemplazar_post_completo(client):
    datos = {"id": 1, "title": "Nuevo titulo", "body": "Nuevo cuerpo", "userId": 1}

    respuesta = client.reemplazar_post(1, datos)

    assert respuesta.status_code == 200
    assert respuesta.json()["title"] == "Nuevo titulo"
    assert respuesta.json()["body"] == "Nuevo cuerpo"


def test_actualizar_solo_el_titulo(client):
    respuesta = client.actualizar_post(1, {"title": "Solo cambia el titulo"})

    assert respuesta.status_code == 200
    actualizado = respuesta.json()
    assert actualizado["title"] == "Solo cambia el titulo"
    # PATCH no debe borrar los campos que no se enviaron
    assert "body" in actualizado
    assert "userId" in actualizado


def test_borrar_post(client):
    respuesta = client.borrar_post(1)

    assert respuesta.status_code == 200