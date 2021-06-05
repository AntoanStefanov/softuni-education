class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self  # Защо тук не мога да напиша self.iterable

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.iterable) # Ето така върти всеки път 20 ред
            raise StopIteration()
        return self.iterable[self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
# При втори завъртване индекса си е -1 и не можем . Как се оправя това?
# Всеки път при фор цикъл да върти ?
for item in reversed_list:
    print(item)
