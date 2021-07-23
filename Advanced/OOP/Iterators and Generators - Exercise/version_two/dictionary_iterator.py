class dictionary_iter:
    def __init__(self, dict_obj):
        self.tuples = list(dict_obj.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.tuples):
            raise StopIteration()

        current_index = self.index
        self.index += 1
        current_tuple = self.tuples[current_index]
        return current_tuple



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
