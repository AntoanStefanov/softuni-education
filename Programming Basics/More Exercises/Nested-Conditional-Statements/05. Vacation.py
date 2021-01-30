budget = float(input())
season = input()
if budget <= 1000:
    place = "Camp"

    if season == "Summer":
        destination = "Alaska"
        destination_price = budget * 0.65
    else:
        destination = "Morocco"
        destination_price = budget * 0.45
elif 1000 < budget <= 3000:
    place = "Hut"

    if season == "Summer":
        destination = "Alaska"
        destination_price = budget * 0.80
    else:
        destination = "Morocco"
        destination_price = budget * 0.60
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        destination = "Alaska"
    else:
        destination = "Morocco"
    destination_price = budget * 0.90

print(f"{destination} - {place} - {destination_price:.2f}")
