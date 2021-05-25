n = int(input())
unique_elements = set()
for _ in range(n):
    elements = tuple(input().split())

    for el in elements:
        unique_elements.add(el)

[print(el) for el in unique_elements]


###################### SECOND SOL #

n = int(input())

elements = set()
for _ in range(n):
    current_elements = input().split()
    elements.update(current_elements)

[print(element) for element in elements]
