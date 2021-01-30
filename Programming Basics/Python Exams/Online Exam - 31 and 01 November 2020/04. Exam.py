top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail = 0
total_mark = 0
number_of_students = int(input())

for student in range(1, number_of_students + 1):
    mark = float(input())

    if mark >= 5:
        top_students += 1
    elif mark >= 4:
        between_4_and_5 += 1
    elif mark >= 3:
        between_3_and_4 += 1
    elif mark < 3:
        fail += 1
    total_mark += mark

print(f"Top students: {top_students / number_of_students * 100:.2f}%")
print(
    f"Between 4.00 and 4.99: {between_4_and_5 / number_of_students * 100:.2f}%")
print(
    f"Between 3.00 and 3.99: {between_3_and_4 / number_of_students * 100:.2f}%")
print(f"Fail: {fail / number_of_students * 100:.2f}%")
print(f"Average: {total_mark / number_of_students:.2f}")
