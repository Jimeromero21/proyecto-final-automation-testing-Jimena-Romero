import pytest


def test_listar_usuarios(client):
    respuesta = client.listar_usuarios()

    assert respuesta.status_code == 200
    usuarios = respuesta.json()
    assert len(usuarios) == 10


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_usuario_tiene_campos_basicos(client, user_id):
    respuesta = client.obtener_usuario(user_id)

    assert respuesta.status_code == 200
    usuario = respuesta.json()
    assert usuario["id"] == user_id
    for campo in ("name", "username", "email"):
        assert campo in usuario, f"Falta el campo {campo}"
    assert "@" in usuario["email"]


def test_posts_de_usuario_le_pertenecen(client):
    respuesta = client.posts_de_usuario(2)

    assert respuesta.status_code == 200
    posts = respuesta.json()
    assert len(posts) > 0
    assert all(p["userId"] == 2 for p in posts)


def test_usuario_inexistente(client):
    assert client.obtener_usuario(999).status_code == 404