import math
from math import sqrt
vacation = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
mini = int(input())
truck = int(input())
num_toys = puzzle+doll+bear+mini+truck
sum = (puzzle*2.60)+(doll*3)+(bear*4.10)+(mini*8.20)+(truck*2)
if num_toys >= 50:
    sum = sum-(sum*0.25)
rent = sum*0.10
profit = sum-rent
left = sqrt((profit-vacation)**2)
g = f"{left:.2f}"
if profit >= vacation:
    print(f'Yes! {g} lv left.')
else:
    print(f'Not enough money! {g} lv needed.')
