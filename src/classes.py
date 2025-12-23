class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализая Product"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_object: dict):
        """Метод, который должен принимать на вход параметры товара в словаре и возвращать созданный объект класса"""

        name, description, price, quantity = new_object.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер возвращает значение приватного атрибута цены"""

        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер устанавливает новое значение приватного атрибута цены"""
        if new_price > 0:
           self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

class Smartphone(Product):
    name: str
    description: str
    price: float
    quantity: int
    efficiency: float
    model: str
    memory: float
    color: str
    
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: float, color: str):
        """Инициалиация Smartphone"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self. color = color

class LawnGrass(Product):
    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """Инициалиация LawnGrass"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color





class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация Category"""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        count = 0
        for product in self.__products:
            count += int(product.quantity)
        return f"{self.name}, количество продуктов: {count} шт."

    def add_product(self, other):
            """Для добавления товаров в категорию"""

            if isinstance(other, Product):
                self.__products.append(other)
                Category.product_count += 1
            else:
                raise TypeError

    @property
    def products(self):
        """Геттер, который будет выводить список товаров в виде строк"""

        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product



