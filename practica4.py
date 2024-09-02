"""
Crea una aplicación de mensajería donde el servicio de notificaciones puede ser sustituido por diferentes
implementaciones (por ejemplo, notificaciones por correo electrónico o SMS) usando inyección de dependencias.

Requisitos:
Define una interfaz INotificationService con un método send_notification(recipient: str, message: str) -> None.
Crea dos implementaciones: EmailNotificationService y SMSNotificationService.
Crea una clase MessagingService que acepte un objeto INotificationService en su constructor y lo use para
 enviar notificaciones.
"""
from typing import Protocol

# 1. Define la interfaz
class INotificationService(Protocol):
    def send_notification(self, recipient: str, message: str) -> None:
        ...

# 2. Implementa la interfaz con diferentes servicios
class EmailNotificationService:
    def send_notification(self, recipient: str, message: str) -> None:
        print(f"Enviando correo a {recipient}: {message}")

class SMSNotificationService:
    def send_notification(self, recipient: str, message: str) -> None:
        print(f"Enviando SMS a {recipient}: {message}")

# 3. Clase que usa la inyección de dependencias
class MessagingService:
    def __init__(self, notification_service: INotificationService):
        self._notification_service = notification_service

    def send_message(self, recipient: str, message: str) -> None:
        self._notification_service.send_notification(recipient, message)

# Uso
email_service = EmailNotificationService()
sms_service = SMSNotificationService()

messaging_service_email = MessagingService(email_service)
messaging_service_sms = MessagingService(sms_service)

messaging_service_email.send_message("user@example.com", "Hello via Email!")
messaging_service_sms.send_message("+123456789", "Hello via SMS!")
