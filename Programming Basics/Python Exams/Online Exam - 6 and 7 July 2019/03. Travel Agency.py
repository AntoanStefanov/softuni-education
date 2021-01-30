# 1.	Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# 2.	Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# 4.	Дни за престой - цяло число в интервала [1 … 10000]


town = input()
packet_type = input()
vip_discount = input()
days = int(input())

day_price = 0
is_valid = True
if not days < 1:

    if town == "Bansko" or town == "Borovets":
        if packet_type == "withEquipment":
            day_price = 100
            if vip_discount == "yes":
                day_price -= day_price * 0.10
        elif packet_type == "noEquipment":
            day_price = 80
            if vip_discount == "yes":
                day_price -= day_price * 0.05
        else:
            is_valid = False

    elif town == "Varna" or town == "Burgas":
        if packet_type == "withBreakfast":
            day_price = 130
            if vip_discount == "yes":
                day_price -= day_price * 0.12
        elif packet_type == "noBreakfast":
            day_price = 100
            if vip_discount == "yes":
                day_price -= day_price * 0.07
        else:
            is_valid = False
    else:
        is_valid = False

    if not is_valid:
        print("Invalid input!")
    else:
        total_price = day_price * days

        if days > 7:
            total_price -= day_price

        print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print("Days must be positive number!")
