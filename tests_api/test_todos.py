def test_filtrar_todos_completados(client):
    respuesta = client.listar_todos(completed="true")

    assert respuesta.status_code == 200
    todos = respuesta.json()
    assert len(todos) > 0
    assert all(t["completed"] is True for t in todos)


def test_filtrar_todos_de_un_usuario_pendientes(client):
    respuesta = client.listar_todos(userId=1, completed="false")

    assert respuesta.status_code == 200
    todos = respuesta.json()
    assert all(t["userId"] == 1 and t["completed"] is False for t in todos)