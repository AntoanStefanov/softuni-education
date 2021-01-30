command = input()
prime_sum = 0
non_prime_sum = 0
while command != "stop":

    number = int(command)

    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    for i in range(2, number):  # почваме от 2 , защото трябва да се дели на 1
        # и не вкл. самото число защото и на него трябва да се дели простото число.
        if number % i == 0:
            non_prime_sum += number
            break
    else:
        prime_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
