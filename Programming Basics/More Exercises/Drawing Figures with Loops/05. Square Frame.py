n = int(input())
x = (n - 2) * "- "
print(f"+ {x}+")
for row in range(2, n):
    print(f"| {x}|")
print(f"+ {x}+")
