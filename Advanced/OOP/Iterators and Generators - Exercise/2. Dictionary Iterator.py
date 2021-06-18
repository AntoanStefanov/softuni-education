class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.keys = list(self.dict)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == len(self.dict):
            raise StopIteration()
        current_key = self.keys[self.current_index]
        current_value = self.dict[current_key]
        self.current_index += 1
        return current_key, current_value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Питай Инес за Итераторите,
#  ако завъртим два фор цикъла при даден итератор втория ще бъде празен,
#  ако сме пипали атрибутите на обекта ? Така ли трябва да е ?
#  И защо не го правим така, че
# Да се въртят n на брой цикли ?
for x in result:
    print(x)


# my way 

class dictionary_iter:
    def __init__(self, dict):
        self.tuples = list(dict.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.tuples:
            raise StopIteration()
        current_tuple = self.tuples[0]
        self.tuples = self.tuples[1:]
        return current_tuple
