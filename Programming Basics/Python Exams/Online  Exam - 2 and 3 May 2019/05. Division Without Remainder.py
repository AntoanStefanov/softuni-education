n = int(input())


p1_numbers = 0
p2_numbers = 0
p3_numbers = 0


for i in range(1, n + 1):
    number = int(input())

    if number % 2 == 0:
        p1_numbers += 1
    if number % 3 == 0:
        p2_numbers += 1
    if number % 4 == 0:
        p3_numbers += 1


p1 = (p1_numbers / n) * 100
p2 = (p2_numbers / n) * 100
p3 = (p3_numbers / n) * 100


print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
