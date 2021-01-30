tournament_days = int(input())

total_money = 0
total_wins = 0
total_loses = 0

for i in range(tournament_days):
    sport = input()
    money_for_the_day = 0
    wins = 0
    loses = 0
    while sport != "Finish":
        state = input()
        if state == "win":
            money_for_the_day += 20
            wins += 1
        else:
            loses += 1

        sport = input()
    if sport == "Finish":
        if wins > loses:
            money_for_the_day += money_for_the_day * 0.10
        total_money += money_for_the_day
        total_wins += wins
        total_loses += loses

if total_wins > total_loses:
    total_money += total_money * 0.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
