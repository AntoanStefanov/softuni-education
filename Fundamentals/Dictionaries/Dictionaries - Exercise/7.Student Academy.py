# My solution
# n = int(input())

# students = {}

# for _ in range(n):
#     student_name = input()
#     grade = float(input())

#     if student_name not in students:
#         students[student_name] = []

#     students[student_name].append(grade)


# for student, grades in students.items():
#     average_grade = sum(grades) / len(grades)

#     grades.clear()

#     if average_grade >= 4.50:
#         grades.append(average_grade)

# passing_students = students.copy()

# for student, grades in students.items():

#     if len(grades) == 0:
#         passing_students.pop(student)


# for student, grade in passing_students.items():
#     mark = float(grade[0])
#     del grade[0]
#     passing_students[student] = mark


# sorted_passing_students = dict(
#     sorted(passing_students.items(), key=lambda recieved_tuple: -recieved_tuple[1]))


# for student, mark in sorted_passing_students.items():
#     print(f"{student} -> {mark:.2f}")


n = int(input())

students = {}

for i in range(n):

    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

# Dictionary  comprehension no lambda
# Връща key:value в случая value e израза за вземане на average grade
# passing_students = {student: sum(grades) / len(grades) for student,
#                     grades in students.items() if sum(grades) / len(grades) >= 4.50}

# Dictionary  comprehension with lambda


def get_average(grades): return sum(
    grades) / len(grades)


passing_students = {student: get_average(grades) for student,
                    grades in students.items() if get_average(grades) >= 4.50}


# Without Dictionary  comprehension

# for student, grades in students.items():
#     average_grade = sum(grades) / len(grades)

#     if average_grade >= 4.50:
#         passing_students[student] = average_grade

sorted_passing_students = dict(sorted(
    passing_students.items(), key=lambda recieved_tuple: -recieved_tuple[1]))


for student, grade in sorted_passing_students.items():

    print(f"{student} -> {grade:.2f}")
