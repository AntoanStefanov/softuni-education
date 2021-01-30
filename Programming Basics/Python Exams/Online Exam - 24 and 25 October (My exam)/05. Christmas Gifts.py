age = input()
kids = 0
adults = 0

while age != "Christmas":
    age = int(age)

    if age <= 16:
        kids += 1
    else:
        adults += 1

    age = input()

toys_price = kids * 5
shirts_price = adults * 15


print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys_price}")
print(f"Money for sweaters: {shirts_price}")
