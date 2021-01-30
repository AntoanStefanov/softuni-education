number_of_companies = int(input())
most_passengers_company = ""
most_passengers = 0
for company in range(1, number_of_companies + 1):

    company_name = input()
    number_of_passengers = input()
    total_passengers = 0
    flights = 0

    while number_of_passengers != "Finish":
        number_of_passengers = int(number_of_passengers)

        total_passengers += number_of_passengers
        flights += 1

        number_of_passengers = input()

    average_number_of_passengers = total_passengers // flights
    print(f"{company_name}: {average_number_of_passengers} passengers.")

    if average_number_of_passengers > most_passengers:
        most_passengers_company = company_name
        most_passengers = average_number_of_passengers

print(f"{most_passengers_company} has most passengers per flight: {most_passengers}")
