import json
from src.task import Category
from src.loader import load_data_from_json


def test_load_data_from_json(tmp_path):
    # Сброс счётчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создаем тестовый JSON-объект
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Телефоны для связи",
            "products": [
                {
                    "name": "iPhone",
                    "description": "Смартфон Apple",
                    "price": 100000.0,
                    "quantity": 5
                },
                {
                    "name": "Samsung",
                    "description": "Смартфон Samsung",
                    "price": 80000.0,
                    "quantity": 3
                }
            ]
        }
    ]

    # Сохраняем JSON-файл во временную папку
    json_path = tmp_path / "test_products.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    # Загружаем данные через функцию
    categories = load_data_from_json(str(json_path))

    # Проверки
    assert len(categories) == 1
    cat = categories[0]
    assert cat.name == "Смартфоны"
    assert cat.description == "Телефоны для связи"
    assert len(cat.products) == 2

    assert cat.products[0].name == "iPhone"
    assert cat.products[1].price == 80000.0

    assert Category.category_count == 1
    assert Category.product_count == 2
