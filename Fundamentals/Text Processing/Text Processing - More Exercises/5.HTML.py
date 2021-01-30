title = input()

content = input()

print('<h1>')
print('   ', title)
print('</h1>')
print('<article>')
print('   ', content)
print('</article>')

while True:
    comment = input()
    if comment == 'end of comments':
        break
    print('<div>')
    print('   ', comment)
    print('</div>')
