class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, remove_quantity):
        if self.quantity >= remove_quantity:
            self.quantity -= remove_quantity

    def increase(self, add_quantity):
        self.quantity += add_quantity
