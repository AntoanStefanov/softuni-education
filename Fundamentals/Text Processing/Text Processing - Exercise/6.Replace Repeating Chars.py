string = input()


for i, ch in enumerate(string):
    if i + 1 == len(string) or  ch != string[i + 1]:
        print(f"{ch}", end="")
