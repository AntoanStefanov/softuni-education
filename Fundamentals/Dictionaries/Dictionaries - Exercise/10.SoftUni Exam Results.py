
username_points = {}
language_submissions = {}
while True:
    data = input()
    if data == "exam finished":
        break

    elif 'banned' in data:
        user, command = data.split('-')
        del username_points[user]
        continue

    else:
        user, language, points = data.split("-")
        points = int(points)

        if user not in username_points:
            username_points[user] = 0

        if points > username_points[user]:
            username_points[user] = points

        if language not in language_submissions:
            language_submissions[language] = 0

        language_submissions[language] += 1


sorted_username_points = dict(
    sorted(username_points.items(), key=lambda t: (-t[1], t[0])))
print("Results:")
for username, points in sorted_username_points.items():
    print(f"{username} | {points}")


sorted_language_submissions = dict(
    sorted(language_submissions.items(), key=lambda t: (-t[1], t[0])))


print("Submissions:")
for language, points in sorted_language_submissions.items():
    print(f"{language} - {points}")
