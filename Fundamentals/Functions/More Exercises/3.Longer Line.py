from math import sqrt


def closest_point(x1, y1, x2, y2):

    first_line = sqrt(x1**2 + y1**2)
    second_line = sqrt(x2**2 + y2**2)
    if first_line > second_line:
        print(f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})")
    else:
        print(f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    # double firstLine = Math.Sqrt(Math.Pow(Math.Abs(a-c), 2) + Math.Pow(Math.Abs(b-d), 2));
    first_line = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    second_line = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)

    if first_line >= second_line:
        closest_point(x1, y1, x2, y2)
    else:
        closest_point(x3, y3, x4, y4)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
