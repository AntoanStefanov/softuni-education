# Adding the name in the set directly , if the name already exists,
# it doesn't add second of the same name. 

number_of_names = int(input())
names = set()
for _ in range(number_of_names):
    name = input()
    names.add(name)

for name in names:
    print(name)


############ List and Set ##


number_of_names = int(input())
names = []
for _ in range(number_of_names):
    name = input()
    names.append(name)
set_names = set(names)
for name in set_names:
    print(name)
