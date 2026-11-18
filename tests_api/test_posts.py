def test_filtrar_posts_por_usuario(client):
    respuesta = client.listar_posts(userId=3)

    assert respuesta.status_code == 200
    posts = respuesta.json()
    assert len(posts) > 0
    assert all(p["userId"] == 3 for p in posts), \
        "ERROR: hay posts de otro usuario en el filtro"


def test_post_inexistente_devuelve_404(client):
    respuesta = client.obtener_post(99999)

    assert respuesta.status_code == 404


def test_comentarios_pertenecen_al_post(client):
    respuesta = client.comentarios_de_post(1)

    assert respuesta.status_code == 200
    comentarios = respuesta.json()
    assert len(comentarios) > 0
    assert all(c["postId"] == 1 for c in comentarios)


def test_respuesta_es_json(client):
    respuesta = client.obtener_post(1)

    assert "application/json" in respuesta.headers["Content-Type"]