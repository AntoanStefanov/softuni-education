def number_increment(numbers):

    def increase():
        incremented_numbers = []
        for num in numbers:
            incremented_numbers.append(num + 1)
        return incremented_numbers

    return increase()


print(number_increment([1, 2, 3]))
