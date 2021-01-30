contests = {}
total_users_points = {}
while True:
    data = input()
    if data == "no more time":
        break
    username, contest, points = data.split(' -> ')
    points = int(points)

    if contest not in contests.keys():
        contests[contest] = [[username, points]]
    else:
        is_participant = False
        for info in contests[contest]:
            if info[0] == username:
                if info[1] < points:
                    info[1] = points
                is_participant = True
                break
        if not is_participant:
            contests[contest].append([username, points])

for contest in contests:
    for info in contests[contest]:
        if info[0] not in total_users_points.keys():
            total_users_points[info[0]] = 0
        total_users_points[info[0]] += info[1]


for contest, info in contests.items():
    participants = 0
    for user, points in info:
        participants += 1
    print(f"{contest}: {participants} participants")
    info = sorted(info, key=lambda t: (-t[1], t[0]))
    number = 1
    for user, points in info:
        print(f"{number}. {user} <::> {points}")
        number += 1

print("Individual standings:")
total_users_points = dict(
    sorted(total_users_points.items(), key=lambda t: (-t[1], t[0])))
number = 1
for user, total_points in total_users_points.items():
    print(f"{number}. {user} -> {total_points}")
    number += 1
