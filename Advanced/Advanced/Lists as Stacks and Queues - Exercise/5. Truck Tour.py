from collections import deque
petrol_pumps = int(input())
pumps = deque()
for petrol_pump in range(petrol_pumps):

    liters, km_to_next_pump = input().split()
    liters = int(liters)
    km_to_next_pump = int(km_to_next_pump)
    pumps.append(liters - km_to_next_pump)

original_pumps = pumps.copy()

tank = 0
previous_pumps = deque()
while pumps:
    if pumps[0] < 0:
        pumps.append(pumps.popleft())
    else:
        while True:
            current_pump = pumps.popleft()

            if tank + current_pump >= 0:
                tank += current_pump
                previous_pumps.append(current_pump)
                if not pumps:
                    get_this_index = previous_pumps.popleft()
                    break

            else:
                tank = 0
                pumps.appendleft(current_pump)
                pumps.extend(previous_pumps)
                previous_pumps.clear()
                break

print(original_pumps.index(get_this_index))


################ SECOND SOLUTION #############

number_of_pumps = int(input())


pumps = deque()

for pump in range(number_of_pumps):
    petrol, next_pump_distance = [int(x) for x in input().split()]
    pumps.append(petrol - next_pump_distance)

initial_pumps = pumps.copy()
passed_pumps = deque()
tank = 0

while pumps:
    pump = pumps.popleft()
    passed_pumps.append(pump)
    tank += pump
    if tank < 0:
        tank = 0
        while passed_pumps:
            pumps.append(passed_pumps.popleft())
        passed_pumps = deque()

print(initial_pumps.index(passed_pumps[0]))
