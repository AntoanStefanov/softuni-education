degrees = int(input())
time = input()
outfit = ""
shoes = ""
if time == "Morning" and 10 <= degrees <= 18:
    outfit += "Sweatshirt"
    shoes += "Sneakers"
elif time == "Afternoon" and 10 <= degrees <= 18:
    outfit += "Shirt"
    shoes += "Moccasins"
elif time == "Evening" and 10 <= degrees <= 18:
    outfit += "Shirt"
    shoes += "Moccasins"

elif time == "Morning" and 18 < degrees <= 24:
    outfit += "Shirt"
    shoes += "Moccasins"
elif time == "Afternoon" and 18 < degrees <= 24:
    outfit += "T-Shirt"
    shoes += "Sandals"
elif time == "Evening" and 18 < degrees <= 24:
    outfit += "Shirt"
    shoes += "Moccasins"

elif time == "Morning" and degrees >= 25:
    outfit += "T-Shirt"
    shoes += "Sandals"
elif time == "Afternoon" and degrees >= 25:
    outfit += "Swim Suit"
    shoes += "Barefoot"
elif time == "Evening" and degrees >= 25:
    outfit += "Shirt"
    shoes += "Moccasins"


print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
