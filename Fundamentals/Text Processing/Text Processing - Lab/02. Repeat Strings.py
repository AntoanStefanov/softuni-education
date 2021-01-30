def repeat_string():
    words = input().split()
    string_list = ''
    for word in words:
        string_list += len(word) * word
    return string_list


print(repeat_string())
