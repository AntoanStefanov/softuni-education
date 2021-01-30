n = int(input())

first_sum = 0
second_sum = 0

for n in range(1, n + 1):
    first_numbers = int(input())
    first_sum += first_numbers

for j in range(1, n + 1):
    second_numbers = int(input())
    second_sum += second_numbers


if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f"No, diff = {abs(first_sum - second_sum)}")


###### OR #########


n = int(input())

left_sum = 0
right_sum = 0

for i in range(2*n):
    if i < n:
        left_numbers = int(input())
        left_sum += left_numbers
    else:
        right_numbers = int(input())
        right_sum += right_numbers


if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")
