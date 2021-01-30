number_of_students = int(input())
total_lectures = int(input())
initial_bonus = int(input())
max_student_bonus = 0
max_student_bonus_attendances = 0
for student in range(number_of_students):
    student_attendances = int(input())
    student_bonus = student_attendances / total_lectures * (5 + initial_bonus)
    if student_bonus > max_student_bonus:
        max_student_bonus = student_bonus
        max_student_bonus_attendances = student_attendances

print(f"Max Bonus: {round(max_student_bonus)}.")
print(f"The student has attended {max_student_bonus_attendances} lectures.")


