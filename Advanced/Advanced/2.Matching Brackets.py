expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == '(':
        stack.append(index)

    elif expression[index] == ')':
        opening_bracket_index = stack.pop()

        print(expression[opening_bracket_index:index + 1])
