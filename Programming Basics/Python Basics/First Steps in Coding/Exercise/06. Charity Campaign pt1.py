campaign_days = int(input())
cooks = int(input())
number_cakes = int(input())
number_waffles = int(input())
number_pancakes = int(input())


cake_money_per_day = number_cakes * 45
waffle_money_per_day = number_waffles * 5.80
pancake_money_per_day = number_pancakes * 3.20

total_money_per_day = (
    cake_money_per_day+waffle_money_per_day+pancake_money_per_day) * cooks

total_money_of_campaign = total_money_per_day*campaign_days
expenses = total_money_of_campaign * 1/8
total_money_after_expenses = total_money_of_campaign - expenses

print(total_money_after_expenses)
