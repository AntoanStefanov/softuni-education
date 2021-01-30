command = input()
cFound = False
oFound = False
nFound = False
word = ""
while command != "End":
    if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        if command == "c":
            if cFound:
                word += command
            else:
                cFound = True
        elif command == "o":
            if oFound:
                word += command
            else:
                oFound = True
        elif command == "n":
            if nFound:
                word += command
            else:
                nFound = True
        else:
            word += command
        if cFound and oFound and nFound:
            print(f"{word}", end=" ")
            word = ""
            cFound = False
            oFound = False
            nFound = False
    command = input()


################## ORR ################
symbol = input()
word = ""
total_phrase = ""
is_c_found = False
is_o_found = False
is_n_found = False
while symbol != "End":
    if 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
        if symbol == "c" and not is_c_found:
            is_c_found = True
            symbol = ""
        elif symbol == "o" and not is_o_found:
            is_o_found = True
            symbol = ""
        elif symbol == "n" and not is_n_found:
            is_n_found = True
            symbol = ""

        if is_c_found and is_o_found and is_n_found:
            total_phrase += word
            is_c_found = False
            is_o_found = False
            is_n_found = False
            word = " "

        word += symbol
        symbol = input()
    else:
        symbol = input()

print(total_phrase)
