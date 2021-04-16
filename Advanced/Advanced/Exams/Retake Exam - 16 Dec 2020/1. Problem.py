from collections import deque


males = [int(v) for v in input().split()]
females = deque(int(v) for v in input().split())

matches = 0

while males and females:

    while males and males[-1] <= 0:
        males.pop()
    while females and females[0] <= 0:
        females.popleft()
    while males and males[-1] % 25 == 0:
        males.pop()
        males.pop()
    while females and females[0] % 25 == 0:
        females.popleft()
        females.popleft()

    if females and males:
        female = females.popleft()
        if female == males[-1]:
            matches += 1
            males.pop()
        else:
            males[-1] -= 2


print(f'Matches: {matches}')
if males:
    males.reverse()
    print(f'Males left: {", ".join([str(x) for x in males])}')
else:
    print(f'Males left: none')
if females:
    print(f'Females left: {", ".join([str(x) for x in females])}')
else:
    print(f'Females left: none')
