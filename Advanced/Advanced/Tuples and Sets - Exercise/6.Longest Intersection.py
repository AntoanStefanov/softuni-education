n = int(input())

longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split('-')
    first_range = first_range.split(',')
    first_start = int(first_range[0])
    first_end = int(first_range[1])
    second_range = second_range.split(',')
    second_start = int(second_range[0])
    second_end = int(second_range[1])

    first_set = set()
    second_set = set()

    for num in range(first_start, first_end + 1):
        first_set.add(num)

    for num in range(second_start, second_end + 1):
        second_set.add(num)

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(
    f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')


############### SECOND TIME #######

n = int(input())
longest_intersection = set()
for _ in range(n):
    first_range, second_range = input().split('-')
    first_range_start, first_range_end = [
        int(x) for x in first_range.split(',')]
    second_range_start, second_range_end = [
        int(x) for x in second_range.split(',')]

    first_set = set(range(first_range_start, first_range_end + 1))
    second_set = set(range(second_range_start, second_range_end + 1))

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(
    f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
