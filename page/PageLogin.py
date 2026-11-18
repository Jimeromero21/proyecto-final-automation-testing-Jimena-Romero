from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class PageLogin:
    def __init__(self, driver):
        self.driver = driver

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.mensaje_error = (By.CSS_SELECTOR, "[data-test='error']")

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username).send_keys(usuario)

    def ingresar_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def hacer_login(self):
        self.driver.find_element(*self.login_button).click()

    def iniciar_sesion(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_login()

    def login_exitoso(self, timeout=10):
        # Espera a que cargue el inventario o aparezca un error, lo que pase primero
        WebDriverWait(self.driver, timeout).until(
            lambda d: "/inventory.html" in d.current_url
            or d.find_elements(*self.mensaje_error)
        )
        return "/inventory.html" in self.driver.current_url