# language: es
Característica: Inicio de sesión

  @smoke
  Escenario: Login exitoso con usuario válido
    Dado que estoy en la página de login
    Cuando inicio sesión con "standard_user" y "secret_sauce"
    Entonces veo la página de inventario

  @regression
  Escenario: Login con clave incorrecta
    Dado que estoy en la página de login
    Cuando inicio sesión con "standard_user" y "clave_incorrecta"
    Entonces no puedo ingresar al inventario

  @regression
  Escenario: Login con usuario bloqueado
    Dado que estoy en la página de login
    Cuando inicio sesión con "locked_out_user" y "secret_sauce"
    Entonces no puedo ingresar al inventario