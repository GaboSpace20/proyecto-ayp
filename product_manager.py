class Product:
    def __init__(self, name, description, price, category, stock, compatible_models=None):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
        self.compatible_models = compatible_models or []
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "stock": self.stock,
            "compatible_models": self.compatible_models,
        }


# Clase para gestionar la lista de productos
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, **filters):
        results = self.products
        if 'category' in filters:
            results = [p for p in results if p.category == filters['category']]
        if 'price' in filters:
            results = [p for p in results if p.price <= filters['price']]
        if 'name' in filters:
            results = [p for p in results if filters['name'].lower() in p.name.lower()]
        if 'in_stock' in filters:
            results = [p for p in results if p.stock > 0]
        return results

    def update_product(self, name, **updates):
        for product in self.products:
            if product.name == name:
                for key, value in updates.items():
                    setattr(product, key, value)
                return product
        return None

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]

    def to_dict(self):
        return [product.to_dict() for product in self.products]


# Crear instancias y manejar productos como prueba inicial
product_manager = ProductManager()

# Agregar productos
product_manager.add_product(Product("Aceite 10W40", "Aceite para motor", 15.99, "aceites", 100))
product_manager.add_product(Product("Filtro de Aire", "Filtro para motor", 10.49, "filtros", 50))

# Buscar productos por categoría
found_products = product_manager.find_product(category="aceites")

# Actualizar producto
product_manager.update_product("Aceite 10W40", stock=90)

# Eliminar producto
product_manager.remove_product("Filtro de Aire")

# Representación en JSON
product_data = product_manager.to_dict()
product_data

def load_products_from_api(self, api_data):
    for item in api_data.get("products", []):
        self.add_product(
            name=item["name"],
            description=item["description"],
            price=item["price"],
            category=item["category"],
            stock=item["stock"]
        )