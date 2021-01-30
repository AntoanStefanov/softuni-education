number_of_students = int(input())

total_exam_mark = 0
top_students = 0
very_good_students = 0
good_students = 0
bad_students = 0

for student in range(1, number_of_students + 1):
    exam_mark = float(input())

    if exam_mark < 3:
        bad_students += 1
    elif exam_mark < 4:
        good_students += 1
    elif exam_mark < 5:
        very_good_students += 1
    else:
        top_students += 1
    total_exam_mark += exam_mark


top_students_percentage = top_students / number_of_students * 100
very_good_students_percentage = very_good_students / number_of_students * 100
good_students_percentage = good_students / number_of_students * 100
bad_students_percentage = bad_students / number_of_students * 100

average_exam_mark = total_exam_mark / number_of_students

print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_students_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {good_students_percentage:.2f}%")
print(f"Fail: {bad_students_percentage:.2f}%")

print(f"Average: {average_exam_mark:.2f}")


######### OR ##########

number_of_students = int(input())

top_students = 0
very_good_students = 0
good_students = 0
bad_students = 0
total_grade = 0

for i in range(1, number_of_students + 1):
    student_grade = float(input())

    if student_grade >= 5:
        top_students += 1
    elif 4 <= student_grade < 5:
        very_good_students += 1
    elif 3 <= student_grade < 4:
        good_students += 1
    elif 2 <= student_grade < 3:
        bad_students += 1
    total_grade += student_grade

print(f"Top students: {top_students / (number_of_students / 100):.2f}%")
print(
    f"Between 4.00 and 4.99: {very_good_students / (number_of_students / 100):.2f}%")
print(
    f"Between 3.00 and 3.99: {good_students / (number_of_students / 100):.2f}%")
print(f"Fail: {bad_students / (number_of_students / 100):.2f}%")
print(f"Average: {total_grade / number_of_students:.2f}")
