string = input()
double_string = ""
for i in range(len(string)):
    double_string += string[i] + string[i]
print(double_string)


######### OR #########


string = input()
double_string = ""
for i in range(len(string)):
    double_char = string[i] + string[i]
    double_string += double_char
print(double_string)

# ######## OR ########

string = input()
double_string = ""

for symbol in string:
    double_string += 2 * symbol
print(double_string)


########## OR #########

string = input()
double_string = ""

for symbol in string:
    double_string += symbol + symbol
print(double_string)


######## OR #######

string = input()
double_string = ""
for i in range(len(string)):
    double_char = 2 * string[i]
    double_string += double_char
print(double_string)


############# OR #######

string = input()
double_string = ""
for i in range(len(string)):
    double_string += 2 * string[i]
print(double_string)
