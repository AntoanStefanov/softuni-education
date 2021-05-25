n = int(input())
usernames = set()
for _ in range(n):
    username = input()
    usernames.add(username)

print('\n'.join(usernames))


### SECOND SOLUTION ### 

n = int(input())
unique_names = set([input() for _ in range(n)])
print('\n'.join(unique_names))
