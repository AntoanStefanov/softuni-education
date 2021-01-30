# read input
rent = int(input())

# calculate
cake = rent * (20/100)
beverages = cake - (cake * (45/100))
animator = rent * 1/3
budget = rent + cake + beverages + animator
# print
print(budget)
