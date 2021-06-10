with open('numbers.txt', 'r') as file:
    result = 0
    for line in file:
        result += int(line)
    print(result)
