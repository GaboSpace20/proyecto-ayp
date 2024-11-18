import json
import requests  

from product_manager import ProductManager
from client_manager import ClientManager
from sale_manager import SaleManager
from payment_manager import PaymentManager
from shipment_manager import ShipmentManager

class OnlineStore:
    def __init__(self):
        self.product_manager = ProductManager()
        self.client_manager = ClientManager()
        self.sale_manager = SaleManager()
        self.payment_manager = PaymentManager()
        self.shipment_manager = ShipmentManager()
        self.products = []  
        self.clients = []
        self.sales = []
        self.payments = []
        self.shipments = []

def add_product(self, name, description, price, category, stock):
    self.product_manager.add_product(name, description, price, category, stock)

def add_client(self, name, id_number, email):
    self.client_manager.add_client(name, id_number, email)

def load_data_from_api(self, api_data):
    self.product_manager.load_products(api_data.get("products", []))
    self.client_manager.load_clients(api_data.get("clients", []))    
    
    # Cargar datos desde API
    def load_data_from_api(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.product_manager.load_products(data.get("products", []))
                self.client_manager.load_clients(data.get("clients", []))
                print("Datos cargados desde la API con éxito.")
            else:
                print(f"Error al cargar datos desde la API: {response.status_code}")
        except Exception as e:
            print(f"Error al conectar con la API: {e}")


def save_to_json(self, filename):
        data = {
            "products": self.products,
            "clients": self.clients,
            "sales": self.sales,
            "payments": self.payments,
            "shipments": self.shipments,
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Datos guardados en {filename}.")

def load_from_json(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.products = data.get("products", [])
                self.clients = data.get("clients", [])
                self.sales = data.get("sales", [])
                self.payments = data.get("payments", [])
                self.shipments = data.get("shipments", [])
            print(f"Datos cargados desde {filename}.")
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado.")

    # Gestión de productos
def add_product(self, name, description, price, category, stock):
        product = {"name": name, "description": description, "price": price, "category": category, "stock": stock}
        self.products.append(product)

def find_product(self, name=None):
        return [p for p in self.products if name.lower() in p["name"].lower()] if name else self.products

    # Gestión de clientes
def add_client(self, name, id_number, email):
        client = {"name": name, "id_number": id_number, "email": email}
        self.clients.append(client)

def find_client(self, id_number=None):
        return [c for c in self.clients if c["id_number"] == id_number] if id_number else self.clients

    # Gestión de ventas
def register_sale(self, client_id, product_name, quantity, payment_method, shipping_service):
        client = self.find_client(client_id)
        product = self.find_product(product_name)
        if client and product and product[0]["stock"] >= quantity:
            sale = {
                "client": client[0],
                "product": product[0],
                "quantity": quantity,
                "payment_method": payment_method,
                "shipping_service": shipping_service,
                "total": product[0]["price"] * quantity,
            }
            product[0]["stock"] -= quantity  # Actualizar stock
            self.sales.append(sale)
            return sale
        return None

    # Indicadores básicos
def sales_summary(self):
        return [{"product": sale["product"]["name"], "quantity": sale["quantity"], "total": sale["total"]} for sale in self.sales]

def top_products(self):
        from collections import Counter
        product_counter = Counter(sale["product"]["name"] for sale in self.sales)
        return product_counter.most_common()

def frequent_clients(self):
        from collections import Counter
        client_counter = Counter(sale["client"]["id_number"] for sale in self.sales)
        return client_counter.most_common()


# Crear instancia de la tienda
store = OnlineStore()

# Integración con la API
api_url = "https://raw.githubusercontent.com/algoritmos-y-Programacion/api-proyecto/main/data.json"
store.load_data_from_api(api_url)

# Guardar y cargar datos
store.save_to_json("store_data.json")
store.load_from_json("store_data.json")

# Pruebas básicas
store.add_client("Juan Pérez", "12345678", "juan@example.com")
store.add_product("Aceite 10W40", "Aceite para motor", 15.99, "aceites", 100)
sale = store.register_sale("12345678", "Aceite 10W40", 2, "contado", "Zoom")
sales_summary = store.sales_summary()

store.products, store.clients, sales_summary
