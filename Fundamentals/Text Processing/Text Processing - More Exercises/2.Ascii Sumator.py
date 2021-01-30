
min_number = ord(input())
max_number = ord(input())
text = input()

# min_number = min(first_char_code, second_char_code)
# max_number = max(first_char_code, second_char_code)

sum_of_chars = 0
for char in text:
    char_number = ord(char)
    if min_number < char_number < max_number:
        sum_of_chars += char_number
print(sum_of_chars)



