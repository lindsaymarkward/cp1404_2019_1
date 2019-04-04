""" Write a list comprehension to produce a new list containing only the products that are on sale (True means it's on sale)
"""


def main():
    products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
    print(products)

    sale_products = get_sale_products(products)
    print(sale_products)


def get_sale_products(products):
    onsale_products = []
    for product in products:
        if product[2]:
            onsale_products.append(product)
    return onsale_products
    # return [product[0] for product in products if product[2]]


main()
