def exchange(a, b):

    print("Before:")
    print(f"a = {a}")
    print(f"b = {b}")

    print("After:")
    print(f"a = {b}")
    print(f"b = {a}")


a = int(input())
b = int(input())

exchange(a, b)
