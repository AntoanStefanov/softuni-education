projection = input()
film_packet = input()
number_of_tickets = int(input())

if projection == "John Wick":
    if film_packet == "Drink":
        ticket = 12
    elif film_packet == "Popcorn":
        ticket = 15
    elif film_packet == "Menu":
        ticket = 19
elif projection == "Star Wars":
    if film_packet == "Drink":
        ticket = 18
    elif film_packet == "Popcorn":
        ticket = 25
    elif film_packet == "Menu":
        ticket = 30
elif projection == "Jumanji":
    if film_packet == "Drink":
        ticket = 9
    elif film_packet == "Popcorn":
        ticket = 11
    elif film_packet == "Menu":
        ticket = 14

total_price = number_of_tickets * ticket

if projection == "Star Wars" and number_of_tickets >= 4:
    total_price *= 0.70
elif projection == "Jumanji" and number_of_tickets == 2:
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")
