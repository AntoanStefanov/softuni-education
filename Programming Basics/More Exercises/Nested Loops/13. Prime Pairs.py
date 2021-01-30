initial_value_of_first_pair = int(input())
initial_value_of_second_pair = int(input())
final_value_of_first_pair = initial_value_of_first_pair + int(input())
final_value_of_second_pair = initial_value_of_second_pair + int(input())


for first_pair in range(initial_value_of_first_pair, final_value_of_first_pair + 1):
    for first in range(2, first_pair):
        if first_pair % first == 0:
            break
    else:
        for second_pair in range(initial_value_of_second_pair, final_value_of_second_pair + 1):
            for second in range(2, second_pair):
                if second_pair % second == 0:
                    break
            else:
                print(f"{first_pair}{second_pair}")
