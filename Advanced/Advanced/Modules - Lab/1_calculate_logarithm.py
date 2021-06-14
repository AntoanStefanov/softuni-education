import math
number = int(input())
base_log = input()
if base_log == 'natural':
    result = math.log(number)
else:
    result = math.log(number, int(base_log))

print(f'{result:.2f}')
