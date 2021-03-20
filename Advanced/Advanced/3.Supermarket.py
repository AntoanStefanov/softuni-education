from collections import deque

queue = deque()

while True:
    name = input()
    if name == 'End':
        print(f"{len(queue)} people remaining.")
        break
    elif name == 'Paid':
        while len(queue) > 0:
            print(queue.popleft())
        continue
    queue.append(name)
