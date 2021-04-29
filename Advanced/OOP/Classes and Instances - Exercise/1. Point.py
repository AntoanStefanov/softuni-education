from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):  # 3, 5 и 10, 2 # FORMULA √((x_2-x_1)²+(y_2-y_1)²)
        # returns the distance between the point and the provided coordinates
        return sqrt(((x - self.x)**2 + (y - self.y)**2))


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
