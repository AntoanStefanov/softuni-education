x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

first_condition = (x1 == x or x2 == x) and y1 <= y <= y2
second_condiotion = (y1 == y or y2 == y) and x1 <= x <= x2

if first_condition or second_condiotion:
    print("Border")
else:
    print("Inside / Outside")
