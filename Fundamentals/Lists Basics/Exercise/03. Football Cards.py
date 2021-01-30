team_A = list(range(1, 12))
team_B = list(range(1, 12))
terminated = False

cards = input()

players_with_cards = cards.split(" ")


for player in players_with_cards:
    player_team, player_number = player.split("-")
    player_number = int(player_number)
    if (player_team == "A") and (player_number in team_A):
        team_A.remove(player_number)
    elif (player_team == "B") and (player_number in team_B):
        team_B.remove(player_number)
    if (len(team_A) or len(team_B)) < 7:
        terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if terminated:
    print("Game was terminated")


######## OR #########


team_A = [f'A-{num}' for num in range(1, 12)]
team_B = [f'B-{num}' for num in range(1, 12)]

cards = input().split()


for card in cards:

    if card in team_A:
        team_A.remove(card)
    elif card in team_B:
        team_B.remove(card)

    if len(team_A) == 6 or len(team_B) == 6:
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
        print('Game was terminated')
        break
else:
    print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
