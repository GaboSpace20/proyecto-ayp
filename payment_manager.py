# Archivo: models/payment.py
from client_manager import Client

class Payment:
    def __init__(self, client, amount, currency, payment_type, payment_date):
        self.client = client
        self.amount = amount
        self.currency = currency  # Moneda del pago
        self.payment_type = payment_type  # Tipo de pago (e.g., Zelle, transferencia)
        self.payment_date = payment_date

    def to_dict(self):
        return {
            "client": self.client.to_dict(),
            "amount": self.amount,
            "currency": self.currency,
            "payment_type": self.payment_type,
            "payment_date": self.payment_date,
        }


class PaymentManager:
    def __init__(self):
        self.payments = []

    def register_payment(self, payment):
        self.payments.append(payment)

    def find_payments(self, **filters):
        results = self.payments
        if 'client' in filters:
            results = [p for p in results if p.client.id_number == filters['client']]
        if 'date' in filters:
            results = [p for p in results if p.payment_date == filters['date']]
        if 'payment_type' in filters:
            results = [p for p in results if p.payment_type.lower() == filters['payment_type'].lower()]
        if 'currency' in filters:
            results = [p for p in results if p.currency.lower() == filters['currency'].lower()]
        return results

    def to_dict(self):
        return [payment.to_dict() for payment in self.payments]


# Crear instancias y manejar pagos como prueba inicial
payment_manager = PaymentManager()

# Crear cliente de prueba
client = Client("Juan Pérez", "12345678", "juan@example.com", "Calle Verdadera 456", "555-6789")

# Registrar un pago
payment = Payment(client, 100.0, "USD", "Zelle", "2024-11-16")
payment_manager.register_payment(payment)

# Buscar pagos por cliente
found_payments = payment_manager.find_payments(client="12345678")

# Representación en JSON
payment_data = payment_manager.to_dict()
payment_data

def register_payment(self, client_id, amount, currency, payment_type):
    client = self.find_client(client_id)
    if not client:
        raise ValueError("Cliente no encontrado.")
