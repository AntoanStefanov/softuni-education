class Appliance:
    def __init__(self, cost: float):  # The cost is for a single day
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * 30
