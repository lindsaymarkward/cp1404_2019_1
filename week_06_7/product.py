class Product:
    """..."""

    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        return "{} ${:.2f} {}".format(self.name, self.price, self.is_on_sale)

    def __repr__(self):
        return str(self)

    def put_on_sale(self, percentage):
        self.is_on_sale = True
        self.price *= ((100 - percentage) / 100)
