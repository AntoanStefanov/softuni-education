# unlimited iterations through
class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count

    def __iter__(self):
        return self.iterator(self)

    class iterator:
        def __init__(self, take_skip_obj):
            self.step = take_skip_obj.step
            self.count = take_skip_obj.count
            self.value = 0


        def __iter__(self):
            return self

        def __next__(self):
            if self.count == 0:
                raise StopIteration()

            value = self.value
            self.value += self.step
            self.count -= 1
            return value


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

for number in numbers:
    print(number)

# For Judge

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration()

        value = self.value
        self.value += self.step
        self.count -= 1
        return value