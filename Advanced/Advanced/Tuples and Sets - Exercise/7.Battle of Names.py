n = int(input())

even_nums = set()
odd_nums = set()

for current_line in range(1, n + 1):

    name = input()
    ascii_name_sum = 0

    for char in name:
        ascii_name_sum += ord(char)

    ascii_name_sum = ascii_name_sum // current_line

    if ascii_name_sum % 2 == 0:
        even_nums.add(ascii_name_sum)
    else:
        odd_nums.add(ascii_name_sum)


even_nums_sum = sum(even_nums)
odd_nums_sum = sum(odd_nums)


if even_nums_sum == odd_nums_sum:
    union_values = odd_nums.union(even_nums)
    print(*union_values, sep=', ')
elif odd_nums_sum > even_nums_sum:
    different_values = odd_nums.difference(even_nums)
    print(*different_values, sep=', ')
elif even_nums_sum > odd_nums_sum:
    symmetric_different_values = odd_nums.symmetric_difference(even_nums)
    print(*symmetric_different_values, sep=', ')
