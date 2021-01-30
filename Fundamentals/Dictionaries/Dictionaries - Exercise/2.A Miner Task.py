task = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in task:
        task[resource] = 0
    task[resource] += quantity


for resource, quantity in task.items():
    print(f"{resource} -> {quantity}")


