days_of_campaign = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
made_cakes = cakes * 45
made_waffles = waffles * 5.80
made_pancakes = pancakes * 3.20
total_sum_per_day = (made_cakes+made_pancakes+made_waffles) * confectioners
total_sum_for_campaign = total_sum_per_day * days_of_campaign
sum_after_expenses = total_sum_for_campaign - (total_sum_for_campaign * 1/8)
print(sum_after_expenses)
