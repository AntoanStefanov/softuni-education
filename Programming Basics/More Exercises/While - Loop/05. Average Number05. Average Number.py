n = int(input())
total = 0
for i in range(1, n + 1):
    number = int(input())
    total += number

average = total / n
print(f"{average:.2f}")


######## OR ########


n = int(input())
sum_numbers = 0
for i in range(n):
    number = int(input())
    sum_numbers += number
print(f"{sum_numbers / n:.2f}")
