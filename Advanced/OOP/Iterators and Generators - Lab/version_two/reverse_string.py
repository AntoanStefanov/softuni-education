def reverse_text(text):
    for chr in reversed(text):
        yield chr


for char in reverse_text("step"):
    print(char, end='')
