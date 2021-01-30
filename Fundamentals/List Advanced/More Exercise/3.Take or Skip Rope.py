string = input()
numbers = []

index = 0

while index < len(string):
    if string[index].isdigit():
        numbers.append(int(string[index]))
        string = string.replace(string[index], '', 1)
        continue
    index += 1

chars = list(string)
take_list = []
skip_list = []


for index, num in enumerate(numbers):
    if index % 2 == 0:
        take_list.append(num)
    else:
        skip_list.append(num)



message = []

for index in range(len(take_list)):
    take_index = take_list[index]
    skip_index = skip_list[index]
    message += chars[:take_index]
    del chars[:take_index]

    del chars[:skip_index]

print("".join(message))
