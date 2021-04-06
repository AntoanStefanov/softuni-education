start = int(input())
end = int(input())


filtered = []
for num in range(start, end + 1):
    for divisor in range(2, 11):
        if num % divisor == 0:
            filtered.append(num)
            break
print(filtered)


# Comprehension

filtered_comprehension = [
    num
    for num in range(start, end + 1)
    if any([num % n == 0 for n in range(2, 11)])
]
print(filtered_comprehension)
