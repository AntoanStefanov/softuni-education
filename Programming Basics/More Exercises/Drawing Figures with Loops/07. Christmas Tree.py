n = int(input())
print(" " * (n + 1) + "|")
for i in range(n):
    print(" "*(n - i - 1) + "*"*(i+1) + " | " +
          "*" * (i + 1) + " " * (n - i - 1))
