neighborhood = [int(house) for house in input().split("@")]

cupid_position = 0


while True:
    jump = input()
    if jump == "Love!":
        break
    command, jump_length = jump.split()

    cupid_position += int(jump_length)
    if cupid_position >= len(neighborhood):
        cupid_position = 0

    if neighborhood[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
        continue

    neighborhood[cupid_position] -= 2

    if neighborhood[cupid_position] == 0:
        print(f"Place {cupid_position} has Valentine's day.")


print(f"Cupid's last position was {cupid_position}.")
failed_places = 0
for house in neighborhood:
    if house != 0:
        failed_places += 1
if failed_places != 0:
    print(f"Cupid has failed {failed_places} places.")
else:
    print("Mission was successful.")
