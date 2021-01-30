jury = int(input())

total_average_mark = 0
number_of_presentations = 0
presentation_name = input()
while presentation_name != "Finish":
    average_presentation_mark = 0
    for person in range(1, jury + 1):
        presentation_mark = float(input())
        average_presentation_mark += presentation_mark
    average_presentation_mark /= jury
    number_of_presentations += 1

    print(f"{presentation_name} - {average_presentation_mark:.2f}.")
    total_average_mark += average_presentation_mark
    presentation_name = input()

total_average_mark /= number_of_presentations

print(f"Student's final assessment is {total_average_mark:.2f}.")
