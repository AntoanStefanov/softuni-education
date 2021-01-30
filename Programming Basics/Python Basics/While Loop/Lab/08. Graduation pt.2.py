name = input()
grade = 1
total_grade = 0
isEjected = False
while grade <= 12:
    year_grade = float(input())
    if year_grade < 4:
        if isEjected:
            print(f"{name} has been excluded at {grade} grade")
            break
        isEjected = True
        continue
    total_grade += year_grade
    grade += 1
else:
    print(f"{name} graduated. Average grade: {total_grade / (grade - 1):.2f}")
