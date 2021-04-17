from collections import deque

integers = deque(int(n) for n in input().split(', '))
needed_index = int(input())
needed_integer = integers[needed_index]
min_num = None
clock_cycles = 0

while True:
    if not integers:
        break
    min_num = min(integers)
    if min_num > needed_integer:
        break
    integers.remove(min_num)
    clock_cycles += min_num


print(clock_cycles)
