film_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())


ticket_price_for_one_day = ticket_price * number_of_tickets
income = ticket_price_for_one_day * number_of_days
cinema_percent = income * cinema_percent / 100
profit = income - cinema_percent

print(f"The profit from the movie {film_name} is {profit:.2f} lv.")
