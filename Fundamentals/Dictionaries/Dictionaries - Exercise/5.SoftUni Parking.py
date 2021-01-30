number_of_commands = int(input())

parking_validation = {}

for _ in range(number_of_commands):
    data = input().split()
    command = data[0]
    username = data[1]

    if command == "register":
        plate_number = data[2]

        if username in parking_validation:
            print(
                f"ERROR: already registered with plate number {plate_number}")
            continue

        parking_validation[username] = plate_number
        print(f"{username} registered {plate_number} successfully")

    elif command == "unregister":

        if username not in parking_validation:
            print(f"ERROR: user {username} not found")
            continue
        parking_validation.pop(username)
        print(f"{username} unregistered successfully")


for username, plate_number in parking_validation.items():
    print(f"{username} => {plate_number}")
