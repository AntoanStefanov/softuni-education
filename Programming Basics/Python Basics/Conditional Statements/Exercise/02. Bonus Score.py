number = int(input())


if number <= 100:
    bonus = 5
elif number > 1000:
    bonus = ((10/100)*number)
elif number > 100:
    bonus = ((20/100) * number)

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

print(bonus)
print(number+bonus)
