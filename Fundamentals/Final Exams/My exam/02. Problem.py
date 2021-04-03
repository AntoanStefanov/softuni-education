import re


pattern = r'!(?P<command>[A-Z][a-z]{2,})!:\[(?P<code>[A-Za-z]{8,})\]'

n = int(input())
# SPACE ?

for _ in range(n):
    to_check = input()

    is_valid = re.finditer(pattern, to_check)
    match = [m for m in is_valid]
    if match:
        for matchh in match:
            command = matchh.group('command')
            code = matchh.group('code')
            decryped = []
            for char in code:
                c = str(ord(char))
                decryped.append(c)
            print(f'{command}: {" ".join(decryped)}')
    else:
        print('The message is invalid')
