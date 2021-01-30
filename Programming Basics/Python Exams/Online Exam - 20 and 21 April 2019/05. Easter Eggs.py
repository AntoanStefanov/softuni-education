number_of_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
max_eggs = 0
max_color = ""

for i in range(1, number_of_eggs + 1):
    color = input()

    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

if max_eggs <= red:
    max_eggs = red
    max_color = "red"
if max_eggs <= blue:
    max_eggs = blue
    max_color = "blue"
if max_eggs <= orange:
    max_eggs = orange
    max_color = "orange"
if max_eggs <= green:
    max_eggs = green
    max_color = "green"


print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_color}")
