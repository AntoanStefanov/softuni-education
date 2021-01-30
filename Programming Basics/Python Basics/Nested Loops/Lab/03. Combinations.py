expected_result = int(input())
combinations = 0
# x1 + x2 + x3 = expected result

for x1 in range(expected_result + 1):
    for x2 in range(expected_result + 1):
        for x3 in range(expected_result + 1):
            if x1 + x2 + x3 == expected_result:
                combinations += 1
print(combinations)
