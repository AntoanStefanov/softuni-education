from collections import deque
from time import strftime, gmtime


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


robots = {}

robots_info = input().split(';')
for r in robots_info:
    robot, time_processing = r.split('-')
    time_processing = int(time_processing)
    is_availabe = True
    available_at = ''
    robots[robot] = [time_processing, is_availabe, available_at]

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
    is_product_taken = False

    for robot, info in robots.items():
        if info[2]:
            if total_seconds == get_sec(info[2]):
                info[1] = True
        time_processing, is_availabe, available_at = info
        if is_availabe:
            is_product_taken = True
            taken_product_at = strftime('%H:%M:%S', gmtime(total_seconds))
            print(f'{robot} - {product} [{taken_product_at}]')

            is_availabe = False
            available_at = strftime('%H:%M:%S', gmtime(
                total_seconds + time_processing))

            info[1] = is_availabe
            info[2] = available_at

            if is_product_taken:
                break
    if not is_product_taken:
        products.append(product)
