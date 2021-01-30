length = float(input())
width = float(input())


# convert length and width to cm

length_cm = length * 100
width_cm = width * 100

desk_width = 70
desk_length = 120

width_cm -= 100  # hallway


non_desks = width_cm % desk_width
desks = width_cm - non_desks
number_desks = desks / desk_width

non_row = length_cm % desk_length
rows = length_cm - non_row
number_rows = rows / desk_length
print(number_rows)

workplaces = number_desks * number_rows - 3

print(int(workplaces))
