raw_key = input()

while True:
    data = input()
    if data == 'Generate':
        break
    data = data.split('>>>')

    command = data[0]

    if command == 'Contains':
        substring = data[1]
        if substring in raw_key:
            print(f'{raw_key} contains {substring}')
        else:
            print("Substring not found!")
    elif command == 'Flip':
        flip_to = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        if flip_to == 'Upper':
            substring = raw_key[start_index:end_index]
            raw_key = raw_key.replace(substring, substring.upper())

        elif flip_to == 'Lower':
            substring = raw_key[start_index:end_index]
            raw_key = raw_key.replace(substring, substring.lower())

        print(raw_key)
    elif command == 'Slice':
        start_index = int(data[1])
        end_index = int(data[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)
print(f'Your activation key is: {raw_key}')
