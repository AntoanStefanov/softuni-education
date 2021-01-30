a = int(input())
b = int(input())
max_generated_passwods = int(input())
generated_passwords = 0
is_enough = False
for A in range(35, 57):
    for B in range(64, 97):

        for x in range(1, a + 1):

            for y in range(1, b + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                if A == 55:
                    A = 34
                if B == 96:
                    B = 63
                A += 1
                B += 1
                generated_passwords += 1
                if (x == a and y == b) or (generated_passwords == max_generated_passwods):
                    is_enough = True
                    break

            if is_enough:
                break
        if is_enough:
            break
    if is_enough:
        break
