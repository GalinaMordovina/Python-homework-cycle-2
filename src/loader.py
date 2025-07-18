import json

from src.task import Category, Product


def load_data_from_json(path: str) -> list[Category]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = []
    for cat in data:
        products = [
            Product(
                prod["name"],
                prod["description"],
                prod["price"],
                prod["quantity"]
            )
            for prod in cat["products"]
        ]
        category = Category(cat["name"], cat["description"], products)
        categories.append(category)

    return categories
