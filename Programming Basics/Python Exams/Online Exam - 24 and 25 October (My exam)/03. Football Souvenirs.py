club = input()
souvenir = input()
number_of_souvenirs = int(input())
invalid_stock = False
invalid_club = False
price = 0
if club == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25
    else:
        invalid_stock = True
elif club == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price = 8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20
    else:
        invalid_stock = True
elif club == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10
    else:
        invalid_stock = True
elif club == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90
    else:
        invalid_stock = True
else:
    invalid_club = True

if invalid_stock:
    print("Invalid stock!")
elif invalid_club:
    print("Invalid country!")
else:
    total_price = number_of_souvenirs * price
    print(
        f"Pepi bought {number_of_souvenirs} {souvenir} of {club} for {total_price:.2f} lv.")
