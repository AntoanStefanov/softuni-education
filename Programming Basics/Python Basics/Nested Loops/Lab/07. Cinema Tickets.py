student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

movie_name = input()
while movie_name != "Finish":
    available_tickets = int(input())
    sold_tickets = 0
    ticket_type = input()
    while ticket_type != "End":
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        sold_tickets += 1
        total_tickets += 1
        if sold_tickets == available_tickets:
            break
        ticket_type = input()
    occupancy_of_the_hall = sold_tickets / available_tickets
    print(f"{movie_name} - {occupancy_of_the_hall:.2%} full.")
    movie_name = input()

student_tickets_percentage = student_tickets / total_tickets
standard_tickets_percentage = standard_tickets / total_tickets
kid_tickets_percentage = kid_tickets / total_tickets

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percentage:.2%} student tickets.")
print(f"{standard_tickets_percentage:.2%} standard tickets.")
print(f"{kid_tickets_percentage:.2%} kids tickets.")
