year = int(input()) + 1
while len(str(year)) != len(set(str(year))):
    year += 1
print(year)

######### OR #########

year = int(input()) + 1

while True:
    if len(str(year)) == len(set(str(year))):
        print(year)
        break
    year += 1
