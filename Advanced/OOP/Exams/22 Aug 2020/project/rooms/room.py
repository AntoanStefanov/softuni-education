class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    #  SHTOM SA TI DLAI PROPERTY GO ZAKACHAI VINAGI !

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value
        # E TUK AKO NE GO ZAKACHISH NA SELFA PISHTI
        # Instance attribute __expenses defined outside __init__

    def calculate_expenses(self, *args):  # Za mesec izchisliqvame , ami za den ako e ?
        total_cost = 0
        total_cost += sum([x.get_monthly_expense() for items in args for x in items])
        self.expenses = total_cost
