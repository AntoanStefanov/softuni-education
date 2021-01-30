# От конзолата се четат следните редове:
# 1.	Височина на стената - цяло число [0… 100]
# 2.	Ширина на стената - цяло число [0… 100]
# 3.	Процент от общата площ на стените, който няма да бъде боядисан - цяло число [5… 95]
# На следващите редове до получаване на командата "Tired!" или докато не бъдат боядисани всички стени, се чете по едно число:
# •	Литри боя – цяло число [0…100]:
# Забележка: Площта за боядисване да бъде закръглена нагоре до най-близкото цяло число.
from math import ceil
wall_height = int(input())
wall_width = int(input())
percent_non_painting_area = int(input())

area = wall_height * wall_width * 4
painting_area = ceil(area - (area * (percent_non_painting_area / 100)))

command = input()


while command != "Tired!":
    liters_paint = int(command)

    painting_area -= liters_paint

    if painting_area < 0:
        print(
            f"All walls are painted and you have {abs(painting_area)} l paint left!")
        break
    elif painting_area == 0:
        print("All walls are painted! Great job, Pesho!")
        break

    command = input()
else:
    print(f"{painting_area} quadratic m left.")
