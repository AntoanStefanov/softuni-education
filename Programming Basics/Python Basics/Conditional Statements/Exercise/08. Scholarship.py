from math import floor
income = float(input())
grade = float(input())
wage = float(input())

social_scholarship = 0
excellent_scholarship = 0

if income < wage and grade > 4.50:
    social_scholarship += 0.35 * wage

if grade >= 5.50:
    excellent_scholarship = grade * 25

if excellent_scholarship >= social_scholarship:
    if excellent_scholarship != 0:
        print(
            f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
    else:
        print("You cannot get a scholarship!")
elif social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")


################### OR #############
# importvash math tuka
income = float(input())
grade = float(input())
salary = float(input())

excellent_scholarship = 0
social_scholarship = 0

if grade >= 5.50:
    excellent_scholarship += grade * 25

if grade > 4.50 and income < salary:
    social_scholarship += 0.35 * salary

if social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif excellent_scholarship >= social_scholarship:
    if excellent_scholarship != 0:
        print(
            f"You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN")
    else:
        print("You cannot get a scholarship!")
