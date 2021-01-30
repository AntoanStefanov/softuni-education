import math
area = 0
shape = input()

if shape == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")

elif shape == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")

elif shape == "circle":
    r = float(input())
    area = r * r * math.pi  # also math.pow(r,2) or r ** 2
    print(f"{area:.3f}")

elif shape == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f"{area:.3f}")
