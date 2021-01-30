number_of_easter_cakes = int(input())
best_baker = ""
best_baker_points = 0

for i in range(1, number_of_easter_cakes + 1):

    total_grade = 0
    name = input()
    points = input()

    while points != "Stop":
        total_grade += int(points)
        points = input()

    print(f"{name} has {total_grade} points.")
    if total_grade > best_baker_points:
        best_baker = name
        best_baker_points = total_grade
        print(f"{name} is the new number 1!")

print(f"{best_baker} won competition with {best_baker_points} points!")
