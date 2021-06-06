def genrange(current_number, end):
    while current_number <= end:
        yield current_number
        current_number += 1

# Може и с for loop
print(list(genrange(1, 10)))

# res [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
