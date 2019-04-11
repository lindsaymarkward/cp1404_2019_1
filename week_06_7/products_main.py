"""
This Product example is a work-in-progress to demonstrate iterative development of classes.
Watch the screencast from the Townsville week 7 lecture. (It is not complete!)
You may like to extend and modify it to continue your learning.
"""
from week_06_7.product import Product

MENU = "A, L, P, Q"
PRODUCT_FILENAME = "products.txt"
ON_SALE_TEXT = "yes"
NOT_ON_SALE_TEXT = "no"


def main():
    products = load_products(PRODUCT_FILENAME)
    print(products)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            print("Add")
        elif choice == "L":
            print(products)
        elif choice == "P":
            put_on_sale(products)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    print(":)")


def load_products(filename):
    products = []
    in_file = open(filename)
    for line in in_file:
        parts = line.split(',')
        # print(repr(parts))
        is_on_sale = True if parts[2].strip() == ON_SALE_TEXT else False
        # print(repr(parts[2]))
        product = Product(parts[0], float(parts[1]), is_on_sale)
        # print(product)
        products.append(product)
    in_file.close()
    return products


def put_on_sale(products):
    choice = int(input("Product: "))
    percentage = float(input("Percentage: "))
    product = products[choice]
    product.put_on_sale(percentage)
    print("You have put the {} on sale.".format(product.name))


main()
