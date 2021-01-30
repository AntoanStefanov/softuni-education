circle = input().split(' ')

count_to_kill = int(input())


new_list = []
counter = 0
index = 0

while len(circle) > 0:
    counter += 1

    if index == len(circle):
        index = 0

    if counter % count_to_kill == 0:
        killed = circle.pop(index)
        new_list.append(killed)
        continue

    index += 1


print(str(new_list).replace('\'', '').replace(' ', ''))

# circle = input().split(' ')
# kill_count = int(input())
# result = []
# counter = 0

# index = 0
# while len(circle) > 0:
#     counter += 1

#     if counter % kill_count == 0:
#         result.append(circle.pop(index))
#     else:
#         index += 1

#     if index >= len(circle):
#         index = 0

# print(str(result).replace(' ', '').replace('\'', ''))
