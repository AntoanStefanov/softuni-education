budget = float(input())
number_of_series = int(input())
total_series_price = 0
for series in range(1, number_of_series + 1):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        series_price *= 0.50
    elif series_name == "Lucifer":
        series_price *= 0.60
    elif series_name == "Protector":
        series_price *= 0.70
    elif series_name == "TotalDrama":
        series_price *= 0.80
    elif series_name == "Area":
        series_price *= 0.90

    total_series_price += series_price


if total_series_price > budget:
    print(
        f"You need {total_series_price-budget:.2f} lv. more to buy the series!")
else:
    print(
        f"You bought all the series and left with {budget-total_series_price:.2f} lv.")
