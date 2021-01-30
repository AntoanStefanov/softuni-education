# help(list)
# print(dir(str))
# x = ''
# help(x.count)


array = [int(el) for el in input().split()]


while True:
    data = input().split()
    command = data[0]
    if command == "end":
        break
    elif command == "decrease":
        for index in range(len(array)):
            array[index] -= 1
        continue
    index_1 = int(data[1])
    index_2 = int(data[2])
    if command == "swap":
        temp = array[index_1]
        array[index_1] = array[index_2]
        array[index_2] = temp
    elif command == "multiply":
        array[index_1] *= array[index_2]
array = [str(el) for el in array]
print(", ".join(array))


    
