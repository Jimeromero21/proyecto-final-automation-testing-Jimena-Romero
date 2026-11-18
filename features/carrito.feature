# language: es
Característica: Carrito de compras

  @smoke
  Escenario: Agregar un producto actualiza el contador
    Dado que inicié sesión con "standard_user"
    Cuando agrego el primer producto
    Entonces el contador del carrito muestra "1"

  @regression
  Escenario: El producto agregado aparece en el carrito
    Dado que inicié sesión con "standard_user"
    Cuando agrego el primer producto
    Y voy al carrito
    Entonces el producto agregado está en el carrito