import pytest

from src.classes import Category, Product


@pytest.fixture
def product():
    return Product(name="Огурцы", description="Обыкновенные огурцы", price=100.0, quantity=1)

@pytest.fixture
def product_2():
    return Product(name="Помидоры", description="Обыкновенные помидоры", price=110.0, quantity=1)


@pytest.fixture
def category():
    return Category(
        name="Овощи",
        description="Обыкновенные овощи",
        products=[
            Product("Огурцы", "Обыкновенные огурцы", 100.0, 1),
            Product("Помироды", "Обыкновенные помидоры", 120.50, 2),
        ]
    )

# @pytest.fixture
# def new_product():
#     return Product("Вещь", "Просто вещь",100500.0,1)