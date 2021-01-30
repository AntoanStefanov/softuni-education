def biggest_number(x, y, z):
    biggest_number = x

    if y > x and y > z:
        return y
    elif z > y and z > x:
        return z
    return biggest_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(biggest_number(first_number, second_number, third_number))
