from math import sqrt


def closest_point(x1, y1, x2, y2):

    first_line = sqrt(x1**2 + y1**2)
    second_line = sqrt(x2**2 + y2**2)
    if first_line <= second_line:
        print(f"({int(x1)}, {int(y1)})")
    else:
        print(f"({int(x2)}, {int(y2)})")


closest_point(float(input()), float(input()), float(input()), float(input()))
