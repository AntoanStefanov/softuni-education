# from collections import deque
# total_food = int(input())

# orders = deque([int(x) for x in input().split()])  # robots_statistics

# # biggest we can use max() also it is for list and robots_statistics
# order = 1
# biggest_order = 0
# while order <= len(orders):
#     current_order = orders.popleft()
#     if current_order > biggest_order:
#         biggest_order = current_order
#     orders.append(current_order)
#     order += 1
# print(biggest_order)


# while orders:
#     order = orders.popleft()
#     if total_food >= order:
#         total_food -= order
#     else:
#         print('Orders left:', end=' ')
#         orders.appendleft(order)
#         print(orders.popleft(), end=' ')
#         break

# else:
#     print('Orders complete')


# WITH robots_statistics INDEX ACCESSING IS IT POSSIBLE = peek deque[0]  ??
# from collections import deque
# total_food = int(input())

# orders = deque([int(x) for x in input().split()])  # robots_statistics


# order = 1
# biggest_order = 0
# while order <= len(orders):
#     current_order = orders.popleft()
#     if current_order > biggest_order:
#         biggest_order = current_order
#     orders.append(current_order)
#     order += 1
# print(biggest_order)


# while orders:
#     if total_food < orders[0]:
#         orders_left = [str(order) for order in orders]
#         print(f"Orders left: {' '.join(orders_left)}")
#         break
#     ordered_food = orders.popleft()
#     total_food -= ordered_food
# else:
#     print('Orders complete')
from collections import deque

food = int(input())
orders = deque([int(order) for order in input().split()])

max_order = max(orders)
print(max_order)
while orders:
    order = orders.popleft()

    if order > food:
        orders.appendleft(order)
        print('Orders left:', end=' ')
        print(*orders)
        break
    food -= order
else:
    print('Orders complete')
