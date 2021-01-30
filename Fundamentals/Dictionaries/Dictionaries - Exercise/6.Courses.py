courses = {}

while True:
    data = input()

    if data == "end":
        break

    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

sorted_courses = dict(
    sorted(courses.items(), key=lambda recieved_tuple: len(recieved_tuple[1]), reverse=True))

for course, students in sorted_courses.items():
    print(f"{course}: {len(students)}")

    sorted_students = sorted(students)

    for student in sorted_students:
        print(f"-- {student}")
