class sequence_repeat:
    def __init__(self, seq, number):
        self.seq = seq
        self.repeat = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.repeat == 0:
            raise StopIteration()
        if self.current_index == len(self.seq):
            self.current_index = 0
        current_element = self.seq[self.current_index]
        self.current_index += 1
        self.repeat -= 1
        return current_element


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

for item in result:
    # Не остава нищо за втори цикъл , а не трябва ли всеки път да има ?
    print(item, end='')
