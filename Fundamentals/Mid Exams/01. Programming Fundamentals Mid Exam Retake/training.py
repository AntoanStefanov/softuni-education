#Problem 1. Bonus Scoring System
 
import math
import sys
 
def total_bonus(attendances, lecturing, additional_bonus ):
    t_bonus = attendances / lecturing * (5 + additional_bonus)
    return t_bonus
 
 
max_n = - sys.maxsize
max_l = 0
# max_l is max_lectures
 
 
number_student = int(input())
lectures = int(input())
course_add_bonus = int(input())
# attendances_per_student = int(input())
 
bonuses_l = []
#lecture_attend = []
 
for individual_student in range (0,number_student):
    attendances_per_student = int(input())
    bonus_student = total_bonus(attendances_per_student,lectures,course_add_bonus)
    rounded_up_bonus= math.ceil(bonus_student)
    bonuses_l.append(rounded_up_bonus)
    #lecture_attend.append(attendances_per_student)
    if bonus_student > max_n:
        max_n = bonus_student
        max_l = attendances_per_student
    else:
        pass
print(f"Max Bonus: {max(bonuses_l)}.")
print(f"The student has attended {max_l} lectures.")