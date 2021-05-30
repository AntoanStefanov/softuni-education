class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        item = str(item)
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        current_list = reversed(self.data)  # <list_reverseiterator .... >
        # Защо join работи тук ? Не е ли само за list със strings ?
        # join([1, 2]) не работи защото 1 и 2 са int ?
        return f"[{', '.join(current_list)}]"


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))  # '[carrot, apple]'
print(stack.pop())  # 'carrot'
print(stack.peek())  # 'apple'
stack.push("cucumber")
print(str(stack))  # '[cucumber, apple]'
print(stack.is_empty())  # False
