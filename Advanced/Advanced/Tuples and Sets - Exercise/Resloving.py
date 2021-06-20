n = int(input())

odd_nums = set()
even_nums = set()

for line in range(1, n + 1):
    name = input()

    sum_ = 0
    for char in name:
        sum_ += ord(char)
    sum_ //= line

    if sum_ % 2 == 0:
        even_nums.add(sum_)
    else:
        odd_nums.add(sum_)

odd_nums_sum = sum(odd_nums)
even_nums_sum = sum(even_nums)


if even_nums_sum == odd_nums_sum:
    union_values = odd_nums | even_nums
    print(', '.join([str(n) for n in union_values]))
elif even_nums_sum < odd_nums_sum:
    different_values = odd_nums - even_nums
    print(', '.join([str(n) for n in different_values]))
elif even_nums_sum > odd_nums_sum:
    symmetric_different_values = odd_nums ^ even_nums
    print(', '.join([str(n) for n in symmetric_different_values]))
