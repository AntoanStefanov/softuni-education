class take_skip:
    def __init__(self, step, count):
        self.current_number = 0
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration()
        temp = self.current_number
        self.current_number += self.step
        self.count -= 1
        return temp


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
