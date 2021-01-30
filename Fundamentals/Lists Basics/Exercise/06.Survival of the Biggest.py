integers = [int(x) for x in input().split()]
numbers_for_remove = int(input())

for iteration in range(numbers_for_remove):
    integers.remove(min(integers))
print(integers)

######################

numbers = [int(num) for num in input().split()]
nums_for_remove = int(input())

while nums_for_remove > 0:
    min_number = min(numbers)
    numbers.remove(min_number)
    nums_for_remove -= 1

print(numbers)

######################

from sys import maxsize
numbers = [int(num) for num in input().split()]
nums_for_remove = int(input())


while nums_for_remove > 0:
    min_number = maxsize
    for num in numbers:
        if num < min_number:
            min_number = num
    numbers.remove(min_number)
    nums_for_remove -= 1

print(numbers)