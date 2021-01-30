numbers_list = [int(x) for x in input().split(", ")]


number_beggars = int(input())
beggars_list = [0] * number_beggars

# Първия for цикъл прави така че да вземе всеки един от всички просяци:
for index_beggar in range(len(beggars_list)):
    # current_beggar е равен на текущия просяк
    current_beggar = index_beggar

    # Тук този for цикъл минава през листа със всички числа които трябва да се разпределят на просяците в зависимост от реда им.
    for index_number in range(len(numbers_list)):

        # current_num проверява чрез %
        current_number = index_number % number_beggars

        # проверява дали е равно на 0, щом е равно на 0 значи се дели на сегашния просяк без остатък и това значи че е той.
        if current_number == current_beggar:

            # След това следващия if проверя дали има пари.
            # Защото ако няма това значи че листа с парите е свършил и на следващите просяци ще дава по 0.
            if beggars_list[index_beggar] == 0:

                # В примерите има някои просяци, които са повече от парите и в този случай е нужен този if.
                if numbers_list[index_number] == 0:

                    beggars_list[current_number] = 0

                    break

                # Aко ли не то под него има там където да се добавят първите пари. Ето това.
                beggars_list[current_number] = numbers_list[index_number]

            # И след това else е щом просяка вече е получавал пари да се добавят към онези.
            else:

                beggars_list[current_number] += numbers_list[index_number]
# И накрая принтира листа който трябва да е output-a на този код.
print(beggars_list)

################## OR ##########


numbers_str = input().split(", ")
numbers = []  # Листа с интегерите и цифрите.

for number in numbers_str:
    number = int(number)
    numbers.append(number)


number_beggars = int(input())
beggars = [0] * number_beggars


position = 0

for number in numbers:

    beggars[position] += number
    position += 1

    if position == len(beggars):
        position = 0

print(beggars)


########### OR ###################


numbers = [int(n) for n in input().split(', ')]
beggars = [0] * int(input())

beggar_index = 0

for number in numbers:

    beggars[beggar_index] += number

    beggar_index += 1

    if beggar_index == len(beggars):
        beggar_index = 0

print(beggars)
