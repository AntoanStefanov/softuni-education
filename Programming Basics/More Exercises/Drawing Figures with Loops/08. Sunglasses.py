num = int(input())

print("*" * (2 * num) + " " * num + "*" * (2 * num))

for row in range(num-2):
    if row == int(((num-1) / 2) - 1):
        print("*" + "/" * ((2 * num) - 2) + "*" +
              "|" * num + "*" + "/" * ((2*num)-2) + "*")
        continue
    print("*" + "/" * ((2*num)-2) + "*" +
          " " * num + "*" + "/" * ((2 * num)-2) + "*")


print("*" * (2 * num) + " " * num + "*" * (2 * num))
