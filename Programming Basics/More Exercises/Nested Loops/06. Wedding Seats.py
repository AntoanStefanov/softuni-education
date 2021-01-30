last_sector = input()
rows_of_sector = int(input())
number_of_seats_on_odd_row = int(input())
number_of_seats_on_even_row = number_of_seats_on_odd_row + 2
seats_counter = 0
for sector in range(65, ord(last_sector) + 1):
    if sector != 65:
        rows_of_sector += 1
    for row in range(1, rows_of_sector + 1):
        if row % 2 == 0:
            number_of_seats = number_of_seats_on_even_row
        else:
            number_of_seats = number_of_seats_on_odd_row
        for seats in range(97, 97 + number_of_seats):
            print(f"{chr(sector)}{row}{chr(seats)}")
            seats_counter += 1
print(seats_counter)

####### OR #########

last_sector = input()
rows_of_sector = int(input())
number_of_seats_on_odd_row = int(input())
seats = 0
for sector in range(65, ord(last_sector) + 1):
    if sector != 65:
        rows_of_sector += 1
    for row in range(1, rows_of_sector + 1):
        if row % 2 == 0:
            for number_of_seats in range(97, (97 + number_of_seats_on_odd_row) + 2):
                print(f"{chr(sector)}{row}{chr(number_of_seats)}")
                seats += 1
        else:
            for number_of_seats in range(97, 97 + number_of_seats_on_odd_row):
                print(f"{chr(sector)}{row}{chr(number_of_seats)}")
                seats += 1
print(seats)

####### OR #########


last_sector = input()
rows_of_sector = int(input())
number_of_seats_on_odd_row = int(input())
seats = 0
for sector in range(65, ord(last_sector) + 1):
    if sector != 65:
        rows_of_sector += 1
    for row in range(1, rows_of_sector + 1):
        if row % 2 == 0:
            for number_of_seats in range(97, (97 + number_of_seats_on_odd_row) + 2):
                print(f"{chr(sector)}{row}{chr(number_of_seats)}")
                seats += 1
        else:
            for number_of_seats in range(97, 97 + number_of_seats_on_odd_row):
                print(f"{chr(sector)}{row}{chr(number_of_seats)}")
                seats += 1
print(seats)
