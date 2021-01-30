limit_of_unsatisfying_grades = int(input())
number_of_unsatisfying_grades = 0

task_name = input()
solved_problems = 0
total_grade = 0
last_problem = ""

while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        number_of_unsatisfying_grades += 1
        if number_of_unsatisfying_grades == limit_of_unsatisfying_grades:
            print(
                f"You need a break, {limit_of_unsatisfying_grades} poor grades.")
            break

    total_grade += grade
    solved_problems += 1
    last_problem = task_name
    task_name = input()
else:
    print(f"Average score: {total_grade / solved_problems:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")
