class sequence_repeat:
    def __init__(self, text, times):
        self.sequence = text
        self.number = times
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration()
        index = self.index
        self.index += 1
        self.number -= 1
        if self.index == len(self.sequence):
            self.index = 0

        return self.sequence[index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
