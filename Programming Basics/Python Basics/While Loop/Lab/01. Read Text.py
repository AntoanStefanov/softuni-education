text = input()

while text != "Stop":
    print(text)
    text = input()


############# or #########


while True:
    line = input()
    if line.lower() == "stop":
        break
    print(line)


########### OR #################

command = ""
while command.capitalize() != "Stop":
    print(command)
    command = input()
