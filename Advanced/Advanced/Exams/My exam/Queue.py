from collections import deque

# chocolates = deque([int(x) for x in input().split(', ')])
# cups_of_milk = deque([int(x) for x in input().split(', ')])

# milkshakes = 0

# while chocolates and cups_of_milk:

#     while chocolates and chocolates[-1] <= 0:
#         chocolates.pop()
#     while cups_of_milk and cups_of_milk[0] <= 0:
#         cups_of_milk.popleft()

#     if chocolates and cups_of_milk:
#         milk = cups_of_milk.popleft()
#         if milk == chocolates[-1]:
#             chocolates.pop()
#             milkshakes += 1
#         else:
#             chocolates[-1] -= 5
#             cups_of_milk.append(milk)
#     if milkshakes == 5:
#         break

# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")

# if chocolates:
#     print(f"Chocolate: {', '.join([str(i) for i in chocolates])}")
# else:
#     print("Chocolate: empty")

# if cups_of_milk:
#     print(f"Milk: {', '.join([str(i) for i in cups_of_milk])}")
# else:
#     print("Milk: empty")


chocolates = deque([int(x) for x in input().split(', ')])
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while True:
    removed = False
    if (not chocolates) or (not cups_of_milk):
        break

    last_chocolate = chocolates[-1]
    first_milk = cups_of_milk[0]

    if last_chocolate <= 0:
        chocolates.pop()
        removed = True

    if first_milk <= 0:
        cups_of_milk.popleft()
        removed = True
    if removed:
        continue

    if last_chocolate == first_milk:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        chocolates[-1] -= 5
        cups_of_milk.append(cups_of_milk.popleft())

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(i) for i in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(i) for i in cups_of_milk])}")
else:
    print("Milk: empty")
