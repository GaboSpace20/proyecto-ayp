from sale_manager import sale

class Shipment:
    def __init__(self, order, shipping_service, cost, delivery_details=None):
        self.order = order  # Referencia a la venta asociada
        self.shipping_service = shipping_service  # e.g., Zoom, Delivery por moto
        self.cost = cost  # Costo del envío
        self.delivery_details = delivery_details  # Información adicional si es delivery por moto

    def to_dict(self):
        return {
            "order": self.order.to_dict(),
            "shipping_service": self.shipping_service,
            "cost": self.cost,
            "delivery_details": self.delivery_details,
        }


class ShipmentManager:
    def __init__(self):
        self.shipments = []

    def register_shipment(self, shipment):
        self.shipments.append(shipment)

    def find_shipments(self, **filters):
        results = self.shipments
        if 'client' in filters:
            results = [s for s in results if s.order.client.id_number == filters['client']]
        if 'date' in filters:
            # Asumimos que el pedido tiene un atributo de fecha asociado
            results = [s for s in results if s.order.date == filters['date']]
        return results

    def to_dict(self):
        return [shipment.to_dict() for shipment in self.shipments]


# Crear instancias y manejar envíos como prueba inicial
shipment_manager = ShipmentManager()


# Registrar un envío
shipment = Shipment(order=sale, shipping_service="Zoom", cost=5.0, delivery_details=None)
shipment_manager.register_shipment(shipment)

# Buscar envíos por cliente
found_shipments = shipment_manager.find_shipments(client="12345678")

# Representación en JSON
shipment_data = shipment_manager.to_dict()
shipment_data

def register_shipment(self, sale, shipping_service, cost):
    if sale not in self.sales:
        raise ValueError("Venta no encontrada para el envío.")