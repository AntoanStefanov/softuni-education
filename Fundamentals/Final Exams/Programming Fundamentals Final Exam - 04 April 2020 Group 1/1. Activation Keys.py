raw_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            old_substring = raw_key[start_index:end_index]
            new_substring = raw_key[start_index:end_index].upper()
            raw_key = raw_key.replace(old_substring, new_substring)

        elif command[1] == "Lower":
            old_substring = raw_key[start_index:end_index]
            new_substring = raw_key[start_index:end_index].lower()
            raw_key = raw_key.replace(old_substring, new_substring)
        print(raw_key)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        part_to_remove = raw_key[start_index:end_index]
        raw_key = raw_key.replace(part_to_remove, '')
        print(raw_key)


print(f"Your activation key is: {raw_key}")
