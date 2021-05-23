from collections import deque
brackets = input()
open_parentheses = []  # stack

for skoba in brackets:

    if not len(brackets) % 2 == 0:
        print('NO')
        break
    if skoba == '(' or skoba == '{' or skoba == '[':
        open_parentheses.append(skoba)
    else:
        last_open_parentheses = open_parentheses.pop()
        pair = last_open_parentheses + skoba
        if pair == '()' or pair == '{}' or pair == '[]':
            continue
        else:
            print('NO')
            break
else:
    print('YES')

########## SECOND SOLUTION ############


brackets = deque(input())
opening_brackets = deque()
closing_brackets = deque()
if len(brackets) % 2 == 1:
    print('NO')
else:
    while brackets:
        bracket = brackets.popleft()

        if bracket == '(' or bracket == '{' or bracket == '[':
            opening_brackets.append(bracket)
        else:
            pair = opening_brackets.pop() + bracket

            if pair == '()' or pair == '[]' or pair == '{}':
                continue
            else:
                print('NO')
                break
    else:
        print('YES')
