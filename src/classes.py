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

    @classmethod
    def new_product(cls, new_object: dict):
        """Метод, которыйпринимать на вход параметры товара в словаре и возвращать созданный объект класса"""

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
           self.__price == new_price
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

    def add_product(self, product: Product):
            """Для добавления товаров в категорию"""

            self.products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        """Геттер, который будет выводить список товаров в виде строк"""

        product = ""
        for product in self.__products:
            product += f"{Product.name}, {Product.price} руб. Остаток: {Product.quantity} шт.\n"
        return product







