
from selenium.webdriver.common.by import By


class PageCart:

    def __init__(self, driver):
        self.driver = driver

        # Localizadores de la página del carrito
        self.titulo_carrito = (By.CLASS_NAME, "title")
        self.productos_carrito = (By.CLASS_NAME, "cart_item")
        self.nombre_producto = (By.CLASS_NAME, "inventory_item_name")
        self.contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.boton_checkout = (By.ID, "checkout")
        self.boton_continuar_comprando = (By.ID, "continue-shopping")

    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo_carrito).text

    def obtener_productos(self):
        return self.driver.find_elements(*self.productos_carrito)

    def obtener_nombres_productos(self):
        return self.driver.find_elements(*self.nombre_producto)

    def checkout_visible(self):
        return self.driver.find_element(*self.boton_checkout).is_displayed()

    def continuar_comprando(self):
        self.driver.find_element(*self.boton_continuar_comprando).click()
