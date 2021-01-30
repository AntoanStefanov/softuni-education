months = int(input())


total_electricity = 0
total_other_bills = 0

for month in range(1, months + 1):
    electricity = float(input())

    other_bills = (electricity + 20 + 15) + (electricity + 20 + 15) * 0.20

    total_electricity += electricity
    total_other_bills += other_bills


water = 20 * months
internet = 15 * months

average_bills = (total_electricity + total_other_bills +
                 water + internet) / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {total_other_bills:.2f} lv")
print(f"Average: {average_bills:.2f} lv")
