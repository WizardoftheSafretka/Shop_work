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
        return self.__price * self.quantity + other.__price * other.quantity

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

    def add_product(self, product: Product):
            """Для добавления товаров в категорию"""

            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        """Геттер, который будет выводить список товаров в виде строк"""

        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product



