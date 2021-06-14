from helper import generate_seq, find_number


while True:
    command = input()
    if command == 'Stop':
        break
    data = command.split()
    if data[0] == 'Create':
        fibonacci_numbers = generate_seq(int(data[-1]))
        print(fibonacci_numbers)
    else:
        print(find_number(int(data[-1]), fibonacci_numbers))
