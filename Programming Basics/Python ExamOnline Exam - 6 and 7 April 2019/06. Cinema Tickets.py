student_tickets = 0
standard_tickets = 0
kid_tickets = 0


movie_name = input()

while movie_name != "Finish":

    available_tickets = int(input())
    ticket_type = input()
    sold_tickets = 0
    while ticket_type != "End":
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        sold_tickets += 1
        if available_tickets == sold_tickets:
            break
        ticket_type = input()

    print(f"{movie_name} - {sold_tickets / available_tickets:.2%} full.")

    movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets:.2%} student tickets.")
print(f"{standard_tickets / total_tickets:.2%} standard tickets.")
print(f"{kid_tickets / total_tickets:.2%} kids tickets.")
