items = input().split(", ")


while True:
    data = input()
    if data == "Craft!":
        break

    command, item = data.split(" - ")
    
    if command == "Drop":
        if item in items:
            items.remove(item)
    elif command == "Collect":
        if item not in items:
            items.append(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items:
            old_item_index = items.index(old_item) + 1
            items.insert(old_item_index, new_item)
    elif command == "Renew":
        if item in items:
            temp = items.pop(items.index(item))
            items.append(temp)

print(", ".join(items))
