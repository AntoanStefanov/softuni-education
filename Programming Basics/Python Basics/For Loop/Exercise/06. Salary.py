
tabs = int(input())
salary = float(input())


for tab in range(1, tabs + 1):
    website = input()

    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(int(salary))
