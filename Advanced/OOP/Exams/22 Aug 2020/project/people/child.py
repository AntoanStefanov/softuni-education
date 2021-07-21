class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)  # the money that the kid requires for a day

    # Dobaveno ot Doncho
    def get_monthly_expense(self):
        return self.cost * 30
