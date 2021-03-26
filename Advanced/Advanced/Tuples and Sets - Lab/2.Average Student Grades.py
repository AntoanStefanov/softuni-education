from collections import defaultdict
number_of_students = int(input())

student_records = defaultdict(list)

for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    student_records[name].append(grade)

for name, grades in student_records.items():
    average_grade = sum(grades) / len(grades)
    grades = [f'{grade:.2f}' for grade in grades]
    print(f"{name} -> {' '.join(grades)} (avg: {average_grade:.2f})")
