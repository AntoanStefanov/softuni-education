first_number = int(input())
second_number = int(input())
magical_number = int(input())
count = 0
is_found = False
for first in range(first_number, second_number + 1):
    for second in range(first_number, second_number + 1):
        count += 1
        if first + second == magical_number:
            print(
                f"Combination N:{count} ({first} + {second} = {magical_number})")
            is_found = True
            break
    if is_found:
        break
else:
    print(f"{count} combinations - neither equals {magical_number}")
