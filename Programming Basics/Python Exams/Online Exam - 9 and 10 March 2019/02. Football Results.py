wins = 0
loses = 0
drawn = 0

for matches in range(3):
    match_result = input()
    if match_result[0] > match_result[2]:
        wins += 1
    elif match_result[0] < match_result[2]:
        loses += 1
    elif match_result[0] == match_result[2]:
        drawn += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {drawn}")


############# OR #########

first_match_result = input()
second_match_result = input()
third_match_result = input()
wins = 0
loses = 0
drawn = 0


if (first_match_result[0]) > (first_match_result[2]):
    wins += 1
elif (first_match_result[0]) < (first_match_result[2]):
    loses += 1
elif (first_match_result[0]) == (first_match_result[2]):
    drawn += 1

if (second_match_result[0]) > (second_match_result[2]):
    wins += 1
elif (second_match_result[0]) < (second_match_result[2]):
    loses += 1
elif (second_match_result[0]) == (second_match_result[2]):
    drawn += 1

if (third_match_result[0]) > (third_match_result[2]):
    wins += 1
elif (third_match_result[0]) < (third_match_result[2]):
    loses += 1
elif (third_match_result[0]) == (third_match_result[2]):
    drawn += 1


print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f" Drawn games: {drawn}")
