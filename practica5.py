"""
Construye un sistema de procesamiento de pagos modular donde los métodos de pago (por ejemplo, tarjeta de crédito,
PayPal) son inyectados en un servicio de pago principal. Utiliza un contenedor de inyección de dependencias para
gestionar las dependencias.

Requisitos:
Define una interfaz IPaymentProcessor con un método process_payment(amount: float) -> None.
Crea implementaciones como CreditCardProcessor y PayPalProcessor.
Crea una clase PaymentService que acepte un IPaymentProcessor en su constructor.
Utiliza un contenedor de inyección de dependencias (como un simple diccionario) para gestionar las dependencias.
"""

from typing import Protocol, Dict, Type

# 1. Define la interfaz
class IPaymentProcessor(Protocol):
    def process_payment(self, amount: float) -> None:
        ...

# 2. Implementa diferentes procesadores de pago
class CreditCardProcessor:
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor:
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")

# 3. Servicio de pago principal
class PaymentService:
    def __init__(self, processor: IPaymentProcessor):
        self._processor = processor

    def process(self, amount: float) -> None:
        self._processor.process_payment(amount)

# 4. Contenedor de dependencias
class DependencyContainer:
    _dependencies: Dict[str, Type[IPaymentProcessor]] = {}

    @classmethod
    def register(cls, key: str, processor: Type[IPaymentProcessor]):
        cls._dependencies[key] = processor

    @classmethod
    def resolve(cls, key: str) -> IPaymentProcessor:
        processor_class = cls._dependencies.get(key)
        if processor_class:
            return processor_class()
        raise ValueError(f"No processor found for key: {key}")

# Registro de dependencias
DependencyContainer.register("credit_card", CreditCardProcessor)
DependencyContainer.register("paypal", PayPalProcessor)

# Resolución y uso
processor = DependencyContainer.resolve("paypal")
payment_service = PaymentService(processor)
payment_service.process(100.0)
