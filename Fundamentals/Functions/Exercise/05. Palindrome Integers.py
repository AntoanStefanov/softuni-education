def palindrome_checker(number_str):
    return True if number_str == number_str[::-1] else False


num_str_list = input().split(", ")


for num_str in num_str_list:
    print(palindrome_checker(num_str))
