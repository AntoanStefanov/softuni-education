tournament_name = input()
won_games = 0
lost_games = 0
total_games = 0
while tournament_name != "End of tournaments":
    number_of_games = int(input())
    for game in range(1, number_of_games + 1):  # За всеки мач ще получавате
        desi_team_points = int(input())
        enemy_team_points = int(input())
        difference = abs(desi_team_points - enemy_team_points)
        total_games += 1
        if desi_team_points > enemy_team_points:
            print(
                f"Game {game} of tournament {tournament_name}: win with {difference} points.")
            won_games += 1

        elif enemy_team_points > desi_team_points:
            print(
                f"Game {game} of tournament {tournament_name}: lost with {difference} points.")
            lost_games += 1

    tournament_name = input()

print(f"{won_games / total_games:.2%} matches win")
print(f"{lost_games / total_games:.2%} matches lost")
