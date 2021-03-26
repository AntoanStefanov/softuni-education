number_of_names = int(input())
names = []
for _ in range(number_of_names):
    name = input()
    names.append(name)
set_names = set(names)
for name in set_names:
    print(name)

