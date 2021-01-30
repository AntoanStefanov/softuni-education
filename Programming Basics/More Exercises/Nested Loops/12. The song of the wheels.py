# Изключваш 0 , като цифра
control_value = int(input())
counter = 0
password = ""
is_password_found = False
for number in range(1111, 10000):
    number = str(number)

    for index, digit in enumerate(number):
        digit = int(digit)
        if digit == 0:
            break
        elif index == 0:
            a = digit
        elif index == 1:
            b = digit
        elif index == 2:
            c = digit
        elif index == 3:
            d = digit

    if (a < b) and (c > d):
        if (a * b) + (c * d) == control_value:
            counter += 1
            print(number, end=" ")
            if counter == 4:
                password = number
                is_password_found = True

if is_password_found:
    print(f"\nPassword: {password}")
else:
    print("\nNo!")


######## OR #########

control_value = int(input())
counter = 0
is_password_found = False
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b) and (c > d):
                    if (a*b) + (c*d) == control_value:
                        counter += 1
                        print(f"{a}{b}{c}{d}", end=" ")
                        if counter == 4:
                            password = f"{a}{b}{c}{d}"
                            is_password_found = True

if is_password_found:
    print(f"\nPassword: {password}")
else:
    print("\nNo!")
