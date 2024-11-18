from onlinestore import OnlineStore
from product_manager import Product
from client_manager import Client

class Sale:
    def __init__(self, client, products, quantities, payment_method, shipping_method):
        self.client = client
        self.products = products  # Lista de productos comprados
        self.quantities = quantities  # Cantidades de cada producto
        self.payment_method = payment_method
        self.shipping_method = shipping_method
        self.subtotal = self.calculate_subtotal()
        self.discounts = self.calculate_discounts()
        self.iva = self.subtotal * 0.16  # 16% IVA
        self.igtf = self.calculate_igtf()  # 3% IGTF si paga en divisas
        self.total = self.subtotal - self.discounts + self.iva + self.igtf

    def calculate_subtotal(self):
        return sum(product.price * qty for product, qty in zip(self.products, self.quantities))

    def calculate_discounts(self):
        # 5% descuento si el cliente es jurídico y paga de contado
        if self.client.is_business and self.payment_method.lower() == "contado":
            return self.subtotal * 0.05
        return 0

    def calculate_igtf(self):
        # 3% IGTF si paga en divisas
        if self.payment_method.lower() in ["zelle", "paypal", "divisas"]:
            return self.subtotal * 0.03
        return 0

    def to_dict(self):
        return {
            "client": self.client.to_dict(),
            "products": [product.to_dict() for product in self.products],
            "quantities": self.quantities,
            "payment_method": self.payment_method,
            "shipping_method": self.shipping_method,
            "subtotal": self.subtotal,
            "discounts": self.discounts,
            "iva": self.iva,
            "igtf": self.igtf,
            "total": self.total,
        }


class SaleManager:
    def __init__(self):
        self.sales = []

    def register_sale(self, sale):
        self.sales.append(sale)

    def find_sales(self, **filters):
        results = self.sales
        if 'client' in filters:
            results = [s for s in results if s.client.id_number == filters['client']]
        if 'date' in filters:
            # Asumimos que hay un atributo `date` en futuras expansiones
            results = [s for s in results if s.date == filters['date']]
        return results

    def to_dict(self):
        return [sale.to_dict() for sale in self.sales]


# Crear instancias y manejar ventas como prueba inicial
sale_manager = SaleManager()

# Crear productos y cliente de prueba
product1 = Product("Aceite 10W40", "Aceite para motor", 15.99, "aceites", 100)
product2 = Product("Filtro de Aire", "Filtro para motor", 10.49, "filtros", 50)
client = Client("Juan Pérez", "12345678", "juan@example.com", "Calle Verdadera 456", "555-6789")

# Registrar una venta
sale = Sale(client, [product1, product2], [2, 3], payment_method="contado", shipping_method="Zoom")
sale_manager.register_sale(sale)

# Buscar ventas por cliente
found_sales = sale_manager.find_sales(client="12345678")

# Representación en JSON
sale_data = sale_manager.to_dict()
sale_data

def register_sale(self, client_id, product_name, quantity, payment_method, shipping_service):
    client = self.find_client(client_id)
    product = self.find_product(product_name)
    if not client or not product:
        raise ValueError("Cliente o producto no encontrado.")
    if product[0]["stock"] < quantity:
        raise ValueError("Stock insuficiente.")