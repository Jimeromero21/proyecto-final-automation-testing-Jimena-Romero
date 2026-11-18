import requests

from config import API_BASE_URL, API_TIMEOUT


class JsonPlaceholderClient:
    """Cliente para consumir la API de JSONPlaceholder.

    Usa una requests.Session para reutilizar la conexión y los headers
    en todas las llamadas. Cada método devuelve el objeto Response,
    así los tests deciden qué validar (status, body, headers).
    """

    def __init__(self, base_url=API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _request(self, metodo, ruta, **kwargs):
        """Arma la URL completa y ejecuta la solicitud con timeout."""
        url = f"{self.base_url}{ruta}"
        return self.session.request(
            metodo, url, timeout=API_TIMEOUT, **kwargs
        )

    # ---------- Posts ----------
    def listar_posts(self, **filtros):
        """GET /posts. Los filtros se envían como query (ej: userId=3)."""
        return self._request("GET", "/posts", params=filtros)

    def obtener_post(self, post_id):
        """GET /posts/{id}"""
        return self._request("GET", f"/posts/{post_id}")

    def comentarios_de_post(self, post_id):
        """GET /posts/{id}/comments"""
        return self._request("GET", f"/posts/{post_id}/comments")

    def crear_post(self, datos):
        """POST /posts"""
        return self._request("POST", "/posts", json=datos)

    def reemplazar_post(self, post_id, datos):
        """PUT /posts/{id}: reemplaza el recurso completo."""
        return self._request("PUT", f"/posts/{post_id}", json=datos)

    def actualizar_post(self, post_id, datos):
        """PATCH /posts/{id}: modifica solo los campos enviados."""
        return self._request("PATCH", f"/posts/{post_id}", json=datos)

    def borrar_post(self, post_id):
        """DELETE /posts/{id}"""
        return self._request("DELETE", f"/posts/{post_id}")

    # ---------- Users ----------
    def listar_usuarios(self):
        """GET /users"""
        return self._request("GET", "/users")

    def obtener_usuario(self, user_id):
        """GET /users/{id}"""
        return self._request("GET", f"/users/{user_id}")

    def posts_de_usuario(self, user_id):
        """GET /users/{id}/posts"""
        return self._request("GET", f"/users/{user_id}/posts")

    # ---------- Todos ----------
    def listar_todos(self, **filtros):
        """GET /todos. Ej: listar_todos(completed="true")."""
        return self._request("GET", "/todos", params=filtros)