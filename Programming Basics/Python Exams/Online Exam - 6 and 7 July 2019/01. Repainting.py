# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]


nylon_for_sqr_m = int(input()) + 2
paint_in_liters = int(input()) * 1.10
thinner_in_liters = int(input())
work_hours = int(input())

nylon_price = nylon_for_sqr_m * 1.50
paint_price = paint_in_liters * 14.50
thinner_price = thinner_in_liters * 5

total_price = nylon_price + paint_price + thinner_price + 0.40  # торбички

workers_salary = (total_price * 0.30) * work_hours

total_price = total_price + workers_salary
print(f"Total expenses: {total_price:.2f} lv.")
