lines = int(input())
brackets = ''
for _ in range(lines):
    line = input().strip()
    if line == '(' or line == ')':
        brackets += line


balanced = True
for index, bracket in enumerate(brackets):
  
    if index % 2 == 0:
        if bracket == "(":
            if brackets[index+1] == ")":
                continue
            else:
                balanced = False
                break
        else:
            balanced = False
            break

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
