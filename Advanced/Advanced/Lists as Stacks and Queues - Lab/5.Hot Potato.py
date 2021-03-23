# ### WITH LIST ###########

# from collections import deque
# circle = input().split()
# tosses = int(input())

# toss = 0
# index = 0

# while len(circle) > 1:
#     if index == len(circle):
#         index = 0
#     toss += 1
#     if toss == tosses:
#         print(f"Removed {circle.pop(index)}")
#         toss = 0
#         continue

#     index += 1
# print(f"Last is {circle[0]}")

# ###### WITH QUEUE ############

# circle = deque(input().split())
# tosses = int(input())


# toss = 0

# while len(circle) > 1:
#     toss += 1

#     man = circle.popleft()

#     if toss == tosses:
#         print(f'Removed {man}')
#         toss = 0
#     else:
#         circle.append(man)
# print(f'Last is {circle[0]}')

# ######## WITH ROTATE

# from collections import deque

# people = deque(input().split())
# n_toss = int(input())

# while len(people) > 1:
#     people.rotate(-n_toss)
#     loser = people.pop()
#     print(f'Removed {loser}')

# winner = people.pop()

# print(f"Last is {winner}")


###### Jordan   

from collections import deque


people = deque(input().split())
n_toss = int(input())
while len(people) > 1:
    for toss in range(n_toss):
        people.append(people.popleft())
    loser = people.pop()
    print(f"Removed {loser}")

winner = people.pop()
print(f"Last is {winner}")