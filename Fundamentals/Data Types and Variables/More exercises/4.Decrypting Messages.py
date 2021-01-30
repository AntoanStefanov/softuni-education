def decrypt():

    message = []
    key = int(input())
    n = int(input())

    for _ in range(n):
        character = input()
        character = ord(character) + key
        message.append(chr(character))
    decrypted_message = "".join(message)
    return decrypted_message


print(decrypt())
