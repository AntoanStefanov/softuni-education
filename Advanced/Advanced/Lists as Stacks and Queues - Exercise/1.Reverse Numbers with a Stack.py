# My solution
numbers = input().split()

# All methods stack is using - push(append at the end) / pop(removing at the end) = LIFO
stack = []

for index in range(len(numbers) - 1, -1, -1):
    stack.append(numbers[index])  # Pushing into the stack

print(' '.join(stack))


# Sept 2020 - Velizar

inputs = input().split()

stack = []

while inputs:
    next_input = inputs.pop()
    stack.append(next_input)

print(' '.join(stack))


# Second Mine ######################### 2 stacks

stack = input().split(' ')
second_stack = []

while stack:
    second_stack.append(stack.pop())

print(' '.join(second_stack))
