from week_06_7.product import Product


def run_tests():
    # Test empty product
    p1 = Product()
    print(p1)

    # Test initial-value product
    p2 = Product("Name", 100, False)
    print(p2)

    # Test put_on_sale
    p2.put_on_sale(10)
    print(p2.price)  # should be $90
    assert p2.price == 90
    assert p2.is_on_sale


run_tests()
