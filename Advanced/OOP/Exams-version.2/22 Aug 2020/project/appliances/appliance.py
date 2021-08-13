class Appliance:
    def __init__(self, cost):
        self.cost = cost  # cost for 1 day !

    def get_monthly_expense(self):
        return self.cost * 30
