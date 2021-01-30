rent = int(input())

statues = rent * 0.70
catering = statues * 0.85
sounding = catering / 2

total_cost = rent + statues + catering + sounding

print(f"{total_cost:.2f}")
