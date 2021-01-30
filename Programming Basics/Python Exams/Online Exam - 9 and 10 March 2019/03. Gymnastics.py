country = input()
instrument = input()

if country == "Russia":
    if instrument == "ribbon":
        mark = 18.500
    elif instrument == "hoop":
        mark = 19.100
    elif instrument == "rope":
        mark = 18.600
elif country == "Bulgaria":
    if instrument == "ribbon":
        mark = 19.000
    elif instrument == "hoop":
        mark = 19.300
    elif instrument == "rope":
        mark = 18.900
elif country == "Italy":
    if instrument == "ribbon":
        mark = 18.700
    elif instrument == "hoop":
        mark = 18.800
    elif instrument == "rope":
        mark = 18.850

print(f"The team of {country} get {mark:.3f} on {instrument}.")

max_needed_points = 20 - mark

print(f"{(max_needed_points / 20) * 100:.2f}%")
