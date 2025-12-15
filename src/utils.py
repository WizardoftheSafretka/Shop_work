import json
import os.path
from typing import Any

from src.classes import Category, Product


def read_json(path: str) -> Any:
    """Чтение файла"""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list[dict]) -> list[Category]:
    """Создание объектов"""

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
