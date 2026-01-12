import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


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

@pytest.fixture
def smartphone():
    return Smartphone(name="Xiaomi", description="Обыкновенный Xiaomi", price=10000.0, quantity=1,
                      efficiency= 512, model = "F5", memory = 512, color = "Черный")

@pytest.fixture
def lawngrass():
    return LawnGrass(name="Трава", description="Обыкновенная трава", price=5000.0, quantity=1,
                      country =  "Россия", germination_period="5 лет", color="Зеленая")

