try:
    file = open('text.txt', 'r')
    print('File Found')
    # Some implemented code for the opened file
    # ...
    # ...
    file.close()
except FileNotFoundError:
    print('File not found')
