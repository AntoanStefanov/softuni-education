from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]

total_pizzas_made = 0

while pizza_orders and employees:

    pizzas_ordered = pizza_orders.popleft()

    if pizzas_ordered <= 0 or pizzas_ordered > 10:
        continue

    employee_max_pizzas = employees.pop()

    if pizzas_ordered <= employee_max_pizzas:
        total_pizzas_made += pizzas_ordered
        pass
    elif pizzas_ordered > employee_max_pizzas:
        pizzas_ordered -= employee_max_pizzas
        total_pizzas_made += employee_max_pizzas
        pizza_orders.appendleft(pizzas_ordered)

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas_made}')
    print(f'Employees: {", ".join([str(x) for x in employees])}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizza_orders])}')

