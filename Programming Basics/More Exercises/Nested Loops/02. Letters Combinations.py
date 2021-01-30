start = ord(input())
end = ord(input())
dodge = ord(input())

counter = 0

for first_letter in range(start, end + 1):
    for second_letter in range(start, end + 1):
        for third_letter in range(start, end + 1):
            if first_letter == dodge or second_letter == dodge or third_letter == dodge:
                continue
            counter += 1
            print(
                f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
print(counter)
