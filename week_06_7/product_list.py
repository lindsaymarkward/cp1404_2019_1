""" Write a list comprehension to produce a new list containing only the products that are on sale (True means it's on sale)
"""

from week_06_7.product import Product


def main():
    products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
    print(products)

    sale_products = get_sale_products(products)
    print(sale_products)


def get_sale_products(products):
    onsale_products = []
    for product in products:
        if product.is_on_sale:
            onsale_products.append(product)
    return onsale_products
    # return [product for product in products if product[2]]


main()
