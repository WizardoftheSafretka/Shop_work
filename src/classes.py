class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __int__(self, name, description, price, quantity):
        """Инициализая Product"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity




class Category:
    name: str
    description: str
    products: list

    def __int__(self, name, description, produts):
        """Инициализация Category"""

        self.name = name
        self.description = description
        self.products = produts