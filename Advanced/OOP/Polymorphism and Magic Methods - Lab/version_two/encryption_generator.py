class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        res = ''
        for char in self.text:
            encoded_char = ord(char) + other
            while encoded_char < 32:
                encoded_char += 95
            while encoded_char > 126:
                encoded_char -= 95

            res += chr(encoded_char)

        return res


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
