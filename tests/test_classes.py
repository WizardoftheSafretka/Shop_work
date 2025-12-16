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
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

def test_add_product(category, product):
    category.add_product(product)
    assert category.product_count == 5

def test_products(category):
    assert category.products == "Огурцы, 100.0 руб. Остаток: 1 шт.\nПомироды, 120.5 руб. Остаток: 2 шт.\n"