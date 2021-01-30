numbers = map(int, input().split(", "))  # map(функция, iterable)
# index, number е деконструиране на tuple-a, който връща enumerate
# Всичко отдолу е comprehension
print([index for index, number in enumerate(numbers) if number % 2 == 0])


### OR ###


# БРУТАЛИСТ
print([index for index, number in enumerate(
    map(int, input().split(", "))) if number % 2 == 0])
