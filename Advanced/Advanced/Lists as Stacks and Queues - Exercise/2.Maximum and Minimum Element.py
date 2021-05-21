stack = []

numbers_of_queries = int(input())

for _ in range(numbers_of_queries):

    data = input().split()

    type_of_query = data[0]

    if type_of_query == '1':
        element = int(data[1])
        stack.append(element)
    elif type_of_query == '2':
        if stack:
            stack.pop()
    elif type_of_query == '3':
        if stack:
            temp_stack = []
            max_num = 0
            while stack:
                num = stack.pop()
                temp_stack.append(num)
                if num > max_num:
                    max_num = num
            print(max_num)
            while temp_stack:
                stack.append(temp_stack.pop())
    elif type_of_query == '4':
        if stack:
            temp_stack = []
            min_num = 1000
            while stack:
                num = stack.pop()
                temp_stack.append(num)
                if num < min_num:
                    min_num = num
            print(min_num)
            while temp_stack:
                stack.append(temp_stack.pop())

output_stack = []

while stack:
    output_stack.append(stack.pop())
print(*output_stack, sep=', ')


###### with min and max functions ### Second mine solution ###

stack = []

n = int(input())


for _ in range(n):
    command = input()
    if command.startswith('1'):
        element = int(command.split(' ')[1])
        stack.append(element)
    elif stack:
        if command == '2':
            stack.pop()
        elif command == '3':
            print(max(stack))
        elif command == '4':
            print(min(stack))

stack.reverse()
print(', '.join([str(n) for n in stack]))
