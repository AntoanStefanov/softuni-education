contests_and_passwords = {}

user_contest_points = {}

while True:

    command = input()

    if command == 'end of contests':
        break
    contest, password = command.split(':')

    contests_and_passwords[contest] = password


while True:

    data = input()

    if data == 'end of submissions':
        break

    contest, password, username, points = data.split('=>')
    points = int(points)
    first_occurence = True
    if contest in contests_and_passwords.keys():
        if password == contests_and_passwords[contest]:
            if username not in user_contest_points.keys():
                user_contest_points[username] = [[contest, points]]
            else:
                first_occurence = True
                for c in user_contest_points[username]:
                    if c[0] == contest:
                        first_occurence = False
                        if c[1] < points:
                            c[1] = points
                            break
                if first_occurence:
                    user_contest_points[username].append([contest, points])


best_candidate = ''
best_points = 0


for username, info in user_contest_points.items():
    total_points = 0
    for info in user_contest_points[username]:
        total_points += info[1]

    if total_points > best_points:
        best_points = total_points
        best_candidate = username

print(f"Best candidate is {best_candidate} with total {best_points} points.")
print("Ranking:")


user_contest_points = dict(sorted(user_contest_points.items()))
for username, info in user_contest_points.items():
    print(username)

    info = sorted(info, key=lambda x: -x[1])

    for contest, points in info:
        print(f"#  {contest} -> {points}")
