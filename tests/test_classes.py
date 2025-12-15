from src.classes import Category


def test_category_init(category):
    assert category.name == "Овощи"
    assert category.description == "Обыкновенные овощи"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_product_init(product):
    assert product.name == "Огурцы"
    assert product.description == "Обыкновенные огурцы"
    assert product.price == 100.0
    assert product.quantity == 1
