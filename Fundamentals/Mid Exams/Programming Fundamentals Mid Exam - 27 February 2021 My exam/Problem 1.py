from math import ceil
budget = float(input())
students = int(input())
price_of_flour = float(input())
price_of_egg = float(input())
price_of_apron = float(input())

free_packages = 0
for student in range(1, students + 1):
    if student % 5 == 0:
        free_packages += 1

needed_money_for_aprons = price_of_apron * ceil(students + (students * 0.20))
needed_money_for_eggs = price_of_egg * 10 * students
needed_money_for_flour = price_of_flour * (students - free_packages)

total_needed_money = needed_money_for_aprons + \
    needed_money_for_eggs + needed_money_for_flour

if budget >= total_needed_money:
    print(f'Items purchased for {total_needed_money:.2f}$.')
else:
    print(f"{total_needed_money - budget:.2f}$ more needed.")
