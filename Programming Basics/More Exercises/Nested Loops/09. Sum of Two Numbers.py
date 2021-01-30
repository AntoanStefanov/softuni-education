initial_number = int(input())
final_number = int(input())
magical_number = int(input())
combinations = 0
is_found = False
for first_number in range(initial_number, final_number + 1):
    for second_number in range(initial_number, final_number + 1):
        combinations += 1
        if first_number + second_number == magical_number:
            print(
                f"Combination N:{combinations} ({first_number} + {second_number} = {magical_number})")
            is_found = True
            break
    if is_found:
        break


if not is_found:
    print(f"{combinations} combinations - neither equals {magical_number}")
