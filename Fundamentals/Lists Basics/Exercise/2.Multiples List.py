factor = int(input())
count = int(input())

multiples = []

for number in range(1, (factor * count) + 1):
    if number % factor == 0:
        multiples.append(number)

print(multiples)


############ OR #################

factor = int(input())

count = int(input())

multiples = []

number = 1

while count > 0:

    if number % factor == 0:
        multiples.append(number)
        count -= 1

    number += 1

print(multiples)
