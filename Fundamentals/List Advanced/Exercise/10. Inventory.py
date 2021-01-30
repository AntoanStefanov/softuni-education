def collect(item):
    if item not in items:
        items.append(item)


def drop(item):
    if item in items:
        items.remove(item)


def combine_items(item):
    old_item, new_item = item.split(":")

    if old_item in items:
        index = items.index(old_item) + 1
        items.insert(index, new_item)


def renew(item):
    if item in items:
        items.remove(item)
        items.append(item)


def craft(items):

    while True:
        command = input()
        if command == "Craft!":
            break
        command, item = command.split(" - ")

        if command == "Collect":
            collect(item)

        elif command == "Drop":
            drop(item)

        elif command == "Combine Items":
            combine_items(item)

        elif command == "Renew":
            renew(item)

    print(", ".join(items))


items = input().split(", ")
craft(items)
