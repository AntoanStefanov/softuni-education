number_of_strings = int(input())

for number in range(number_of_strings):
    string = input()
    name_start = string.find("@")
    name_end = string.find("|")
    name = string[name_start + 1:name_end]
    age_start = string.index("#")
    age_end = string.index("*")
    age = string[age_start+1:age_end]
    print(f"{name} is {age} years old.")
