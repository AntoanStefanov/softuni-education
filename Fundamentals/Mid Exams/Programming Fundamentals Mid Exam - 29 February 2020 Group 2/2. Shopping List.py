shopping_list = input().split("!")


while True:
    data = input()
    if data == "Go Shopping!":
        break
    data = data.split(" ")
    command = data[0]
    item = data[1]
    if command == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif command == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
    elif command == "Correct":
        new_item = data[2]

        if item in shopping_list:
            index = shopping_list.index(item)
            shopping_list[index] = new_item
    elif command == "Rearrange":
        if item in shopping_list:
            index = shopping_list.index(item)
            temp = shopping_list.pop(index)
            shopping_list.append(temp)
print(", ".join(shopping_list))
