kilometers = int(input())
twenty_four_hours = input()

if kilometers >= 100:
    price = kilometers * 0.06
    print(f"{price:.2f}")
elif kilometers >= 20:
    price = kilometers * 0.09
    print(f"{price:.2f}")
elif kilometers >= 0 and twenty_four_hours == "day":
    price = kilometers * 0.79
    print(f"{0.70 + price:.2f}")
elif kilometers >= 0 and twenty_four_hours == "night":
    price = kilometers * 0.90
    print(f"{0.70 + price:.2f}")
