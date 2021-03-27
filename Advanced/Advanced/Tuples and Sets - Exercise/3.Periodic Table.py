n = int(input())
unique_elements = set()
for _ in range(n):
    elements = tuple(input().split())

    for el in elements:
        unique_elements.add(el)

[print(el) for el in unique_elements]
