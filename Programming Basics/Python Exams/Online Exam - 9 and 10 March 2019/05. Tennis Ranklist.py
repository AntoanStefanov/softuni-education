number_of_tournaments = int(input())
starting_ranklist_points = int(input())

gained_points = 0
won = 0

for tournament in range(1, number_of_tournaments + 1):
    phase_reached = input()

    if phase_reached == "W":
        gained_points += 2000
        won += 1
    elif phase_reached == "F":
        gained_points += 1200
    elif phase_reached == "SF":
        gained_points += 720

total_points = gained_points + starting_ranklist_points
average_points = gained_points / number_of_tournaments
won_percent = (won / number_of_tournaments) * 100


print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")
print(f"{won_percent:.2f}%")
