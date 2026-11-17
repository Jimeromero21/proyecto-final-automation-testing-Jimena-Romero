
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageInventory:

    def __init__(self, driver):
        self.driver = driver

        # Localizadores de la página de inventario
        self.titulo_pagina = (By.CLASS_NAME, "title")
        self.lista_productos = (By.CLASS_NAME, "inventory_list")
        self.nombre_productos = (By.CLASS_NAME, "inventory_item_name")
        self.menu_hamburguesa = (By.ID, "react-burger-menu-btn")
        self.filtro_productos = (By.CLASS_NAME, "product_sort_container")
        self.productos = (By.CLASS_NAME, "inventory_item")
        self.carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")


    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo_pagina).text

    def obtener_productos(self):
        return self.driver.find_elements(*self.nombre_productos)

    def productos_visibles(self):
        return self.driver.find_element(*self.lista_productos).is_displayed()

    def menu_visible(self):
        return self.driver.find_element(*self.menu_hamburguesa).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self.filtro_productos).is_displayed()

    def agregar_primer_producto(self):
        producto = self.driver.find_elements(*self.productos)[0]
        nombre = producto.find_element(*self.nombre_productos).text
        boton = producto.find_element(By.TAG_NAME, "button")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(boton)
        ).click()

        return nombre

    def ir_al_carrito(self):
        self.driver.find_element(*self.carrito).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/cart.html"))

    def obtener_contador_carrito(self):
        return self.driver.find_element(*self.contador_carrito).text


    def quitar_primer_producto(self):
        producto = self.driver.find_elements(*self.productos)[0]
        boton = producto.find_element(By.TAG_NAME, "button")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(boton)
        ).click()

    def esperar_carrito_vacio(self):
        # True si el contador desaparece (carrito vacío)
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.contador_carrito)
        )