parentheses = input()
open_parentheses = []  # stack


for parenthesis in parentheses:
    if not len(parentheses) % 2 == 0:
        print('NO')
        break
    if parenthesis == '(' or parenthesis == '{' or parenthesis == '[':
        open_parentheses.append(parenthesis)
    else:
        last_open_parentheses = open_parentheses.pop()
        pair = last_open_parentheses + parenthesis
        if pair == '()':
            continue
        elif pair == '{}':
            continue
        elif pair == '[]':
            continue
        else:
            print('NO')
            break
else:
    print('YES')
