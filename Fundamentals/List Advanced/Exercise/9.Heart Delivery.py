houses = input().split("@")
houses = [int(n) for n in houses]

cupid_position = 0
valentines = 0

while True:
    command = input().split()

    if command[0] == "Love!":
        break

    length = int(command[1])

    cupid_position += length

    if cupid_position >= len(houses):
        cupid_position = 0

    if houses[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")

    else:

        houses[cupid_position] -= 2

        if houses[cupid_position] == 0:
            print(F"Place {cupid_position} has Valentine's day.")
            valentines += 1


print(f"Cupid's last position was {cupid_position}.")
if valentines == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - valentines} places.")
