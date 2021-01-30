width = int(input())
length = int(input())
heigth = int(input())
total_free_space = width * length * heigth
command = ""
while command != "Done" and total_free_space >= 0:
    command = input()
    if command == "Done":
        break
    total_free_space -= int(command)
if total_free_space >= 0:
    print(f"{total_free_space} Cubic meters left.")
else:
    print(
        f"No more free space! You need {abs(total_free_space)} Cubic meters more.")


########### OR ###########

width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())


free_space = width_free_space * length_free_space * height_free_space
taken_space = 0


while True:

    line = input()
    if line == "Done":
        break

    number_of_boxes = int(line)
    taken_space += number_of_boxes
    if taken_space >= free_space:
        break


left = abs(taken_space - free_space)

if free_space < taken_space:

    print(f"No more free space! You need {left} Cubic meters more.")
else:

    print(f"{left} Cubic meters left.")
 ########## OR #######
appartment_width = int(input())
appartment_length = int(input())
appartment_height = int(input())

free_cubic_meters = appartment_width * appartment_length * appartment_height
taken_cubic_meters = 0

inpt = input()

while inpt != "Done":
    boxes = int(inpt)
    taken_cubic_meters += boxes
    if taken_cubic_meters >= free_cubic_meters:
        break
    inpt = (input())

if free_cubic_meters > taken_cubic_meters:
    left_cubic_meters = free_cubic_meters - taken_cubic_meters
    print(f"{left_cubic_meters} Cubic meters left.")
else:
    needed_cubic_meters = taken_cubic_meters - free_cubic_meters
    print(
        f"No more free space! You need {abs(needed_cubic_meters)} Cubic meters more.")
