player_name = input()
winner = ""
winner_points = 0
while player_name != "Stop":
    player_points = 0
    for letter in range(len(player_name)):
        guessing_number = int(input())
        if guessing_number == ord(player_name[letter]):
            player_points += 10
        else:
            player_points += 2
    if player_points > winner_points:
        winner = player_name
        winner_points = player_points
    elif player_points == winner_points:
        winner = player_name
    player_name = input()
print(f"The winner is {winner} with {winner_points} points!")


######### OR #######


player_name = input()
winner = ""
winner_points = 0
while player_name != "Stop":
    player_points = 0
    for letter in player_name:
        guessing_number = int(input())
        if guessing_number == ord(letter):
            player_points += 10
        else:
            player_points += 2
    if player_points > winner_points:
        winner = player_name
        winner_points = player_points
    elif player_points == winner_points:
        winner = player_name
    player_name = input()
print(f"The winner is {winner} with {winner_points} points!")
