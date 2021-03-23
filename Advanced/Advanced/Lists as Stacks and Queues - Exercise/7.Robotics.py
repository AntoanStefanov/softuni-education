from collections import deque
from time import strftime, gmtime


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


available_robots = deque()
busy_robots = deque()

robots_info = input().split(';')
for r in robots_info:
    robot, time_processing = r.split('-')
    time_processing = int(time_processing)
    available_robots.append([robot, time_processing, True, ''])


start_time = input()
total_seconds = get_sec(start_time)

products = deque()
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)


while products:
    total_seconds += 1
    product = products.popleft()

    if available_robots:
        available_robot = available_robots.popleft()

        print(available_robot)
        available_robot[2] = False
        available_robot[3] = strftime(
            '%H:%M:%S', gmtime(total_seconds + available_robot[1]))
        busy_robots.append(available_robot)
    else:
        products.append(product)
        for busy_robot in busy_robots:
        if get_sec(busy_robot[3]) == total_seconds:
            busy_robot[2] = False