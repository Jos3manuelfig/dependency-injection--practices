"""
Crea un sistema de autenticación simple donde la lógica de validación de usuario y contraseña esté desacoplada del
servicio principal
usando inyección de dependencias.

Requisitos:
Define una interfaz (o clase base) IUserValidator que tenga un método validate(username: str, password: str) -> bool.
Crea una clase SimpleUserValidator que implemente la interfaz IUserValidator.
Crea una clase AuthService que acepte un objeto de tipo IUserValidator en su constructor y lo use para validar usuarios.

"""



from typing import Protocol

# 1. Define la interfaz o clase base
class IUserValidator(Protocol):
    def validate(self, username: str, password: str) -> bool:
        ...

# 2. Implementa la interfaz
class SimpleUserValidator:
    def validate(self, username: str, password: str) -> bool:
        return username == "admin" and password == "1234"

# 3. Clase que usa la inyección de dependencias
class AuthService:
    def __init__(self, validator: IUserValidator):
        self._validator = validator

    def authenticate(self, username: str, password: str) -> bool:
        return self._validator.validate(username, password)

# Uso
validator = SimpleUserValidator()
auth_service = AuthService(validator)
print(auth_service.authenticate("admin", "123"))  # Debería devolver True
