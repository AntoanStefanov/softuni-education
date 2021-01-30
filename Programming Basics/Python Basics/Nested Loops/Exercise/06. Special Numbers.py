number = int(input())

for numbers in range(1111, 9999):
    is_Special = True
    number_as_string = str(numbers)
    for digit in number_as_string:
        if int(digit) == 0:
            is_Special = False
            break
        elif number % int(digit) != 0:
            is_Special = False
            break
    if is_Special:
        print(f"{numbers}", end=" ")


######## OR ########

n = int(input())

for number in range(1111, 10000):
    number = str(number)
    counter = 0
    for digit in number:
        if int(digit) == 0:
            pass
        else:
            if n % int(digit) == 0:
                counter += 1
        if counter == 4:
            print(number, end=" ")


########## OR #############

n = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if (n % i == 0) and (n % j == 0) and (n % k == 0) and (n % m == 0):
                    print(f"{i}{j}{k}{m}", end=" ")
