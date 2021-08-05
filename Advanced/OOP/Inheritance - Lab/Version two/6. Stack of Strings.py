class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        item = str(el)
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        reversed_data = reversed(self.data)
        return f"[{', '.join(reversed_data)}]"


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
