class Client:
    def __init__(self, name, id_number, email, address, phone, is_business=False, contact_name=None, contact_phone=None, contact_email=None):
        self.name = name
        self.id_number = id_number  # Cédula o RIF
        self.email = email
        self.address = address
        self.phone = phone
        self.is_business = is_business  # True si es cliente jurídico
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email

    def to_dict(self):
        return {
            "name": self.name,
            "id_number": self.id_number,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "is_business": self.is_business,
            "contact_name": self.contact_name,
            "contact_phone": self.contact_phone,
            "contact_email": self.contact_email,
        }


class ClientManager:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def find_client(self, **filters):
        results = self.clients
        if 'id_number' in filters:
            results = [c for c in results if c.id_number == filters['id_number']]
        if 'email' in filters:
            results = [c for c in results if c.email.lower() == filters['email'].lower()]
        return results

    def update_client(self, id_number, **updates):
        for client in self.clients:
            if client.id_number == id_number:
                for key, value in updates.items():
                    setattr(client, key, value)
                return client
        return None

    def remove_client(self, id_number):
        self.clients = [c for c in self.clients if c.id_number != id_number]

    def to_dict(self):
        return [client.to_dict() for client in self.clients]


# Crear instancias y manejar clientes como prueba inicial
client_manager = ClientManager()

# Agregar clientes
client_manager.add_client(Client("Juan Pérez", "12345678", "juan@example.com", "Calle Falsa 123", "555-1234"))
client_manager.add_client(Client("Empresa XYZ", "J-98765432", "contacto@xyz.com", "Avenida Principal 456", "555-9876",
                                 is_business=True, contact_name="María Gómez", contact_phone="555-4567", contact_email="maria@xyz.com"))

# Buscar clientes por RIF
found_clients = client_manager.find_client(id_number="12345678")

# Actualizar información del cliente
client_manager.update_client("12345678", address="Calle Verdadera 456", phone="555-6789")

# Eliminar cliente
client_manager.remove_client("J-98765432")

# Representación en JSON
client_data = client_manager.to_dict()
client_data

def load_clients_from_api(self, api_data):
    for client in api_data.get("clients", []):
        self.add_client(
            name=client["name"],
            id_number=client["id_number"],
            email=client["email"]
        )