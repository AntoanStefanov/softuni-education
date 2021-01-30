numbers = [int(n) for n in input().split()]

finish_line_index = len(numbers) // 2

left_racer = numbers[:finish_line_index]

right_racer = numbers[finish_line_index + 1:]
right_racer.reverse()

left_racer_time = 0
right_racer_time = 0

for time in left_racer:
    if time == 0:
        left_racer_time *= 0.8
    left_racer_time += time


for time1 in right_racer:

    if time1 == 0:
        right_racer_time *= 0.8

    right_racer_time += time1

if left_racer_time > right_racer_time:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
else:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
