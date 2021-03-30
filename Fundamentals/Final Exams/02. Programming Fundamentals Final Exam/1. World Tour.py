tour = input()

while True:
    info = input()
    if info == 'Travel':
        break

    info = info.split(':')

    command = info[0]

    if command == 'Add Stop':
        insert_at_index = int(info[1])
        string = info[2]
        if 0 <= insert_at_index < len(tour):
            start_tour = tour[:insert_at_index]
            end_tour = tour[insert_at_index:]
            tour = start_tour + string + end_tour
        print(tour)
    elif command == 'Remove Stop':
        start_index = int(info[1])
        end_index = int(info[2])
        # correct validation INCLUSIVE? what if end index is greater then start index?
        if 0 <= start_index < len(tour) and 0 <= end_index < len(tour):
            tour = tour[:start_index] + tour[end_index + 1:]
        print(tour)
    elif command == 'Switch':
        old_string = info[1]
        new_string = info[2]
        if old_string in tour:
            tour = tour.replace(old_string, new_string)
        print(tour)
print(f"Ready for world tour! Planned stops: {tour}")
