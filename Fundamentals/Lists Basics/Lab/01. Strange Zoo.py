tail = input()
body = input()
head = input()

muskat = [tail, body, head]
muskat[0], muskat[2] = muskat[2], muskat[0]
print(muskat)
