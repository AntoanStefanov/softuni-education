first_set = set()
second_set = set()

numbers_of_first_set, numbers_of_second_set = [int(n) for n in input().split()]

for _ in range(numbers_of_first_set):
    num = int(input())
    first_set.add(num)
for _ in range(numbers_of_second_set):
    num = int(input())
    second_set.add(num)

unique_elements_in_both_sets = first_set & second_set

[print(num) for num in unique_elements_in_both_sets]


########### SECOND SOLUTION #################

first_set_len, second_set_len = [int(x) for x in input().split()]

first_set = set()
second_set = set()

[first_set.add(int(input())) for _ in range(first_set_len)]

[second_set.add(int(input())) for _ in range(second_set_len)]

duplicates_of_both_sets = first_set.intersection(second_set)

[print(num) for num in duplicates_of_both_sets]
