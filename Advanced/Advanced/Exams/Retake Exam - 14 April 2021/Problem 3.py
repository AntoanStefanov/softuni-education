def flights(*args):
    dict = {}
    for index in range(0, len(args), 2):
        destination = args[index]
        if destination == 'Finish':
            break
        if destination not in dict:
            dict[destination] = 0
        dict[destination] += int(args[index+1])

    return dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco',
              98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215,
              'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
