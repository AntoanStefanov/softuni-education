film_name = input()
cinema_hall = input()
number_of_bought_tickets = int(input())


if film_name == "A Star Is Born":
    if cinema_hall == "normal":
        ticket_price = 7.50
    elif cinema_hall == "luxury":
        ticket_price = 10.50
    elif cinema_hall == "ultra luxury":
        ticket_price = 13.50
elif film_name == "Bohemian Rhapsody":
    if cinema_hall == "normal":
        ticket_price = 7.35
    elif cinema_hall == "luxury":
        ticket_price = 9.45
    elif cinema_hall == "ultra luxury":
        ticket_price = 12.75
elif film_name == "Green Book":
    if cinema_hall == "normal":
        ticket_price = 8.15
    elif cinema_hall == "luxury":
        ticket_price = 10.25
    elif cinema_hall == "ultra luxury":
        ticket_price = 13.25
elif film_name == "The Favourite":
    if cinema_hall == "normal":
        ticket_price = 8.75
    elif cinema_hall == "luxury":
        ticket_price = 11.55
    elif cinema_hall == "ultra luxury":
        ticket_price = 13.95

total_price = number_of_bought_tickets * ticket_price

print(f"{film_name} -> {total_price:.2f} lv.")
