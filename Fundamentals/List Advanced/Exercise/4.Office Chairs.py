rooms = int(input())

free_chairs = 0
enough_chairs = True
for room in range(1, rooms + 1):
    tokens = input().split()
    chairs, taken_chairs = len(tokens[0]), int(tokens[1])

    if chairs >= taken_chairs:
        free_chairs += chairs - taken_chairs
    else:
        enough_chairs = False
        print(f"{taken_chairs - chairs} more chairs needed in room {room}")
if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
