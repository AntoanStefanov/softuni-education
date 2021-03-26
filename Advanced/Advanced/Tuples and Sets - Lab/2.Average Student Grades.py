from collections import defaultdict
number_of_students = int(input())

student_records = defaultdict(list)

for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    student_records[name].append(grade)

print(student_records)
for info in student_records.items():
    print(info)
