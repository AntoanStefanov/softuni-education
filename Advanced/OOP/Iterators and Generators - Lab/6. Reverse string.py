# Koe e po pravilno ? 
# Da se popva sled kato globalno promenlivata ne se promenq ili #
# Za vseki sluchai da rabotim s index ? 

# my first time #
def reverse_text(text):
    text = list(text)
    while text:
        yield text.pop()


bebe = 'step'
for char in reverse_text(bebe):
    print(char, end='')

# podava se tovi i popa ne maha gloablnata promenliva bebe a samo text lokalno chisti
print(bebe)

# pets


# ines

def reverse_text(text):
    index = len(text) - 1
    while index >= 0:
        yield text[index]
        index -= 1


for char in reverse_text('step'):
    print(char, end='')
