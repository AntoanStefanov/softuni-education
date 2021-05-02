class Calculator:
    def __init__(self, *args):
        self.numbers = args # self.numbers == tuple


nums = Calculator(1, 2, 3, 4, 5)
print(sum(nums.numbers))
