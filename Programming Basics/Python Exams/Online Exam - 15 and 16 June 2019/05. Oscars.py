actor_name = input()
academy_points = float(input())
jury = int(input())
for person in range(1, jury + 1):
    person_name = input()
    given_points = float(input())

    points_from_person = (len(person_name) * given_points) / 2
    academy_points += points_from_person
    if academy_points > 1250.50:
        print(
            f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.50 - academy_points:.1f} more!")
