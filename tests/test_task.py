from src.task import Product, Category

def test_product_init():
    p = Product("Test", "Desc", 100.5, 2)
    assert p.name == "Test"
    assert p.description == "Desc"
    assert p.price == 100.5
    assert p.quantity == 2

def test_category_init():
    Category.category_count = 0 # счетчики перед тестами, чтобы не сбрасывать
    Category.product_count = 0

    p1 = Product("One", "Desc", 50.0, 1)
    p2 = Product("Two", "Desc", 70.0, 3)

    c = Category("TestCat", "DescCat", [p1, p2])

    assert c.name == "TestCat"
    assert c.description == "DescCat"
    assert len(c.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2
