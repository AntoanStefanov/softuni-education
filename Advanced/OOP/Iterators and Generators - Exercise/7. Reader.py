def read_next(*args):
    container = []
    for arg in args:
        container.extend(list(arg))

    while container:
        yield container[0]
        container = container[1:]


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')


# ines way
def read_next(*args):
    for el in args:
        for sub_el in el:
            yield sub_el


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
