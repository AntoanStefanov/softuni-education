budget = float(input())
season = input()
destination = ""
place = ""
if budget <= 100:
    destination += "Bulgaria"
    if season == "summer":
        # 50 = 50 - (50 * 0.30) = 35 / 50 - 35 =15
        budget -= budget - (budget * 0.30)
        place += "Camp"
    elif season == "winter":
        budget -= budget - (budget * 0.70)
        place += "Hotel"
elif 101 <= budget <= 1000:
    destination += "Balkans"
    if season == "summer":
        budget -= budget - (budget * 0.40)
        place += "Camp"
    elif season == "winter":
        budget -= budget - (budget * 0.80)
        place += "Hotel"
elif budget > 1000:
    destination += "Europe"
    place = "Hotel"
    budget -= budget - (budget * 0.90)


print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")
