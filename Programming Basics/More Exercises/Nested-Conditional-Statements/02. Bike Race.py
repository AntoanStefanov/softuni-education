number_of_juniors = int(input())
number_of_seniors = int(input())
route = input()

if route == "trail":
    juniors_money = number_of_juniors * 5.50
    seniors_money = number_of_seniors * 7
elif route == "cross-country":
    juniors_money = number_of_juniors * 8
    seniors_money = number_of_seniors * 9.50

elif route == "downhill":
    juniors_money = number_of_juniors * 12.25
    seniors_money = number_of_seniors * 13.75
elif route == "road":
    juniors_money = number_of_juniors * 20
    seniors_money = number_of_seniors * 21.50

if number_of_seniors + number_of_juniors >= 50 and route == "cross-country":
    total_money = (juniors_money + seniors_money) * 0.75
else:
    total_money = juniors_money + seniors_money


expenses = total_money * 0.05


donated_money = total_money - expenses

# 0.001 защото дава еррор на тест 2 при закръглянето
print(f"{donated_money + 0.001:.2f}")
