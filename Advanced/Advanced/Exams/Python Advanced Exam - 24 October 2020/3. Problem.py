 ############# WITH DEQUE rotate ############ DEQUE HAS NO SLICING !
from collections import deque
def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    max_pureness = 0
    max_pureness_rotate = None
    for rotate in range(k + 1):
        current_pureness = 0
        for index, num in enumerate(numbers):
            current_pureness += index * num
        if current_pureness > max_pureness:
            max_pureness = current_pureness
            max_pureness_rotate = rotate

        numbers.rotate()  # default n = 1 to right

    return f'Best pureness {max_pureness} after {max_pureness_rotate} rotations'


#################### WITH LISTS AND SLICING #######

# def best_list_pureness(numbers, k):
#     max_pureness = 0
#     max_pureness_rotate = None
#     for rotate in range(k + 1):
#         current_pureness = 0
#         for index, num in enumerate(numbers):
#             current_pureness += index * num
#         if current_pureness > max_pureness:
#             max_pureness = current_pureness
#             max_pureness_rotate = rotate

#         numbers = numbers[-1:] + \
#             numbers[:-1]   # default n = 1 to right

#     return f'Best pureness {max_pureness} after {max_pureness_rotate} rotations'


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
