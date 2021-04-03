capacity = int(input())

records = {}


while True:
    data = input()

    if data == 'Statistics':
        break

    data = data.split('=')

    command = data[0]

    if command == 'Add':
        username = data[1]
        sent_messages = int(data[2])
        recieved_messages = int(data[3])

        if username not in records:
            records[username] = {'sent_messages': sent_messages,
                                 'recieved_messages': recieved_messages}
    elif command == 'Message':
        sender = data[1]
        reciever = data[2]

        if (sender in records) and (reciever in records):
            records[sender]['sent_messages'] += 1
            records[reciever]['recieved_messages'] += 1

            if records[sender]['sent_messages'] + records[sender]['recieved_messages'] == capacity:
                del records[sender]
                print(f'{sender} reached the capacity!')
            if records[reciever]['sent_messages'] + records[reciever]['recieved_messages'] == capacity:
                del records[reciever]
                print(f'{reciever} reached the capacity!')
    elif command == 'Empty':
        username = data[1]

        if username == 'All':
            del records
            records = {}
        else:
            if username in records:
                del records[username]


sorted_records = sorted(
    records.items(), key=lambda x: (-x[1]['recieved_messages'], x[0]))

print(f'Users count: {len(records)}')

for username, messages in sorted_records:
    sent_messages = messages['sent_messages']
    recieved_messages = messages['recieved_messages']
    print(f'{username} - {sent_messages + recieved_messages }')
