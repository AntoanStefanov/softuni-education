# 1.	Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
# 2.	Вид на билета – текст - “Standard”, “Premium” или “VIP”
# 3.	Брой билети – цяло число в интервала [1 … 30]
# 4.	Снимка с трофея – символ – 'Y' (да) или 'N' (не)


tournament_phase = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_photo = input()


if tournament_phase == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
if tournament_phase == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
if tournament_phase == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

all_ticket_price = ticket_price * number_of_tickets

if all_ticket_price > 4000:
    total_price = all_ticket_price * 0.75

elif all_ticket_price > 2500:
    total_price = all_ticket_price * 0.90
else:
    total_price = all_ticket_price

if trophy_photo == "Y" and all_ticket_price <= 4000:
    trophy_price = number_of_tickets * 40
    total_price = total_price + trophy_price
    print(f"{total_price:.2f}")
else:
    print(f"{total_price:.2f}")
