from math import ceil

number_of_easter_cake = int(input())

needed_sugar = 0
needed_flour = 0
max_sugar = 0
max_flour = 0

for i in range(1, number_of_easter_cake + 1):
    spend_sugar = int(input())
    spend_flour = int(input())

    needed_sugar += spend_sugar
    needed_flour += spend_flour

    if spend_sugar > max_sugar:
        max_sugar = spend_sugar
    if spend_flour > max_flour:
        max_flour = spend_flour


print(f"Sugar: {ceil(needed_sugar / 950)}")
print(f"Flour: {ceil(needed_flour / 750)}")
print(
    f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
