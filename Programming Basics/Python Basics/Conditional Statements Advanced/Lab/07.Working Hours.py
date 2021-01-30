hour = int(input())
day = input()


open = 10 <= hour <= 18

if open and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"):
    print("open")
else:
    print("closed")
