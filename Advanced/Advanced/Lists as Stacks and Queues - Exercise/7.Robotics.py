from collections import deque


def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0

    return h, m, s


robots_info = input().split(';')
robot_dict = {}
available_robots = deque()
waiting_robots = deque()
products = deque()

time = [int(x) for x in input().split(':')]

for r in robots_info:
    robot, time_processing = r.split('-')
    time_processing = int(time_processing)
    available_robots.append([robot, time_processing])
    robot_dict[robot] = time_processing


while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:

    for robot in waiting_robots:
        robot_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:  # ако е бил 0 и го намаля с 1 пак тря се върне в свободни роботи
            available_robots.append([robot_name, robot_dict[robot_name]])
    # Понеже през фор , не може да ме маха ще направи филтрация за освобоените роботи
    waiting_robots = [r for r in waiting_robots if r[1] > 0]

    time = next_second(time[0], time[1], time[2])
    product = products.popleft()

    if not available_robots:
        products.append(product)
        continue

    current_robot = available_robots.popleft()
    print(
        f"{current_robot[0]} - {product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
    waiting_robots.append(current_robot)
