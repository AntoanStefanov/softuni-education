people = int(input())
max_people_in_elevator = int(input())

courses = people // max_people_in_elevator

if courses == 0:
    print(1)
else:
    if people % max_people_in_elevator != 0:
        print(courses + 1)
    else:
        print(courses)
