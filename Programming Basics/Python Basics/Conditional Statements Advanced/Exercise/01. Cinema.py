project = input()
rows = int(input())
columns = int(input())
price = 0
if project == "Premiere":
    price = rows * columns * 12
elif project == "Normal":
    price = rows * columns * 7.50
elif project == "Discount":
    price = rows * columns * 5.00
print(f"{price:.2f}")
