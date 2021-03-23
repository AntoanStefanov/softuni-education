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
    for robot, info in robots.items():
        if info[1]:
            print(
                f"{robot} - {products.popleft()} [{strftime('%H:%M:%S', gmtime(total_seconds))}]")
            info[2] = strftime('%H:%M:%S', gmtime(total_seconds + info[0]))
            info[1] = False
            # You need to break loop , flag product and update
        else:
            pass  # Return product , at the end of the queue
        # Test input number 1.
