class vowels:
    def __init__(self, string):
        self.string = string
        self.current_index = 0
        self.end_index = len(string) - 1
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    def __iter__(self):
        return self

    def __next__(self):
        index = self.current_index
        self.current_index += 1
        if index <= self.end_index:
            char = self.string[index]
            if char.lower() in self.vowels:
                return char
                # Защо не излиза с ретърн а чете next ? !!!!!!!!!!!
                # НЕ ИЗЛИЗА СЛЕД ГЛАСНА 'Е' ? !!!!!!!! ЗАЩО БЕЗ РЕТЪРН next(self) не стаа
            next(self) # Тук без return  не става, защо ?
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


class vowels:
    def __init__(self, string):
        self.string = string
        self.current_index = 0
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.string):
            index = self.current_index
            self.current_index += 1
            if self.string[index].lower() in self.vowels:
                return self.string[index]

            return self.__next__()  # така или next(self) е по-добре да се пише ?

        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
