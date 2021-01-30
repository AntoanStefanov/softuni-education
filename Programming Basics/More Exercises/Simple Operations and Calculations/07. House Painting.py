# височина на къщата

x = float(input())

# дължина на страничната стена

y = float(input())

# височината на триъгълната стена на покрива

h = float(input())


# СТЕНИ

side_wall = x * y

window = 1.5 * 1.5

two_side_walls = 2 * side_wall - 2 * window


back_wall = x * x


entrance = 1.2*2

front_and_back_wall = 2 * back_wall - entrance


walls_area = two_side_walls + front_and_back_wall

green_paint = walls_area / 3.4

print(f"{green_paint:.2f}")


# Покрив

two_rectangles = 2 * (x*y)
two_triangles = 2 * (x*h/2)

roof_area = two_rectangles + two_triangles

red_paint = roof_area / 4.3


print(f"{red_paint:.2f}")
