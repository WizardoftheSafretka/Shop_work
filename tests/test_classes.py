import pytest
from pyexpat.errors import messages

from src.classes import Category, Product


def test_category_init(category):
    assert category.name == "Овощи"
    assert category.description == "Обыкновенные овощи"
    assert len(category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_product_init(product):
    assert product.name == "Огурцы"
    assert product.description == "Обыкновенные огурцы"
    assert product.price == 100.0
    assert product.quantity == 1



def test_new_product():
    new_object = {"name": "Вещь", "description": "Просто вещь", "price": 100500.0, "quantity": 1}
    result = Product.new_product(new_object=new_object)
    assert result.name == "Вещь"
    assert result.description == "Просто вещь"
    assert result.price == 100500.0
    assert result.quantity == 1

def test_price(capsys, product):
    assert product.price == 100.0
    product.price = 1
    assert product.price == 1
    product.price = -1
    message = capsys.readouterr()
    assert message.out.strip() == ('Product(Огурцы, Обыкновенные огурцы, 100.0, 1)\n'
 'Цена не должна быть нулевая или отрицательная')

def test_add_product(category, product):
    category.add_product(product)
    assert category.product_count == 5

def test_products(category):
    assert category.products == "Огурцы, 100.0 руб. Остаток: 1 шт.\nПомироды, 120.5 руб. Остаток: 2 шт.\n"

def test_str_product(product):
    assert str(product) == "Огурцы, 100.0 руб. Остаток: 1 шт."

def test_add_products(product, product_2):
    assert product + product_2 == 210.0

def test_category_str(category):
    assert str(category) == 'Овощи, количество продуктов: 3 шт.'

def test_smartphone_init(smartphone):
    assert smartphone.name == "Xiaomi"
    assert smartphone.description == "Обыкновенный Xiaomi"
    assert smartphone.price == 10000.0
    assert smartphone.quantity == 1
    assert smartphone.efficiency == 512
    assert smartphone.model == "F5"
    assert smartphone.memory == 512
    assert smartphone.color == "Черный"

def test_grass_init(lawngrass):
    assert lawngrass.name == "Трава"
    assert lawngrass.description == "Обыкновенная трава"
    assert lawngrass.price == 5000.0
    assert lawngrass.quantity == 1
    assert lawngrass.country == "Россия"
    assert lawngrass.germination_period == "5 лет"
    assert lawngrass.color == "Зеленая"

def test_add_product_error(smartphone):
    with pytest.raises(TypeError):
        result = smartphone + 1

def test_add_category_error(category):
    with pytest.raises(TypeError):
        result = category.add_product(1)

def test_mixin_product(capsys):
    Product("Помидоры", "Обыкновенные помидоры", 110.0, 1)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Помидоры, Обыкновенные помидоры, 110.0, 1)'

def test_init_with_zero_quantity():
    with pytest.raises(ValueError):
        Product(name="Огурцы", description="Обыкновенные огурцы", price=100.0, quantity=0)

def test_middle_middle_price_product(category):
    assert category.middle_price_product() == 110.25

def test_middle_middle_price_product_error():
    error_1 = Category(
        name="Овощи",
        description="Обыкновенные овощи",
        products=[]
    )
    assert error_1.middle_price_product() == 0




