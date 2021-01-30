term_under_the_contract = input()  # Срок на договор
type_of_contact = input()  # Тип на договор
added_mobile_internet = input()  # Добавен мобилен интернет
number_of_months_to_pay = int(input())  # Брой месеци за плащане

is_added_mobile_internet = False


if term_under_the_contract == "one":
    if type_of_contact == "Small":
        price = 9.98
    elif type_of_contact == "Middle":
        price = 18.99
    elif type_of_contact == "Large":
        price = 25.98
    elif type_of_contact == "ExtraLarge":
        price = 35.99
if term_under_the_contract == "two":
    if type_of_contact == "Small":
        price = 8.58
    elif type_of_contact == "Middle":
        price = 17.09
    elif type_of_contact == "Large":
        price = 23.59
    elif type_of_contact == "ExtraLarge":
        price = 31.79


if added_mobile_internet == "yes":
    is_added_mobile_internet = True

if is_added_mobile_internet and price <= 10:
    price += 5.50
elif is_added_mobile_internet and price <= 30:
    price += 4.35
elif is_added_mobile_internet and price > 30:
    price += 3.85

if term_under_the_contract == "two":
    total_sum = (price * number_of_months_to_pay) * 0.9625
else:
    total_sum = price * number_of_months_to_pay


print(f"{total_sum:.2f} lv.")
