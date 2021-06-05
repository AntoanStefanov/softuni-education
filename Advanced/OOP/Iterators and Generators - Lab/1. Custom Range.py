class custom_range:
    def __init__(self, start, end):
        # Taka pri uslovie che start nqma da e nujen kato 0 nikoga
        self.current_value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value <= self.end:
            current_value = self.current_value
            self.current_value += 1
            return current_value
        raise StopIteration()


one_to_ten = custom_range(1, 10)
print(type(one_to_ten))

for num in one_to_ten:
    print(num)

