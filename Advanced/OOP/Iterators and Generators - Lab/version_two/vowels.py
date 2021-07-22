# unlimited iterations over the object.
# class vowels:
#     def __init__(self, string):
#         self.string = string
#
#     def __iter__(self):
#         return self.iterator(self)
#
#     class iterator:
#         vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#
#         def __init__(self, vowels_obj):
#             self.string = vowels_obj.string
#             self.index = 0
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self.index == len(self.string):
#                 raise StopIteration()
#             index = self.index
#             self.index += 1
#             ch = self.string[index]
#             if ch.lower() not in self.vowels:
#                 return self.__next__()
#             return ch
#
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
#
# for char in my_string:
#     print(char)

# For judge
#
# class vowels:
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#
#     def __init__(self, string):
#         self.string = string
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.string):
#             raise StopIteration()
#         index = self.index
#         self.index += 1
#         ch = self.string[index]
#         if ch.lower() not in self.vowels:
#             return self.__next__()
#         return ch

# When we use for loop it's better and easier with generator function

# def vowels_gen(string):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#     index = 0
#     while index < len(string):
#         char = string[index]
#         if char.lower() in vowels:
#             yield string[index]
#         index += 1
#
#     # for ch in string:
#     #     if ch in vowels:
#     #         yield ch
#
#
# for vowel in vowels_gen('Abcedifuty0o'):
#     print(vowel)


# Generator comprehension
def vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return (ch for ch in text if ch.lower() in vowels)

for vowel in vowels('Abcedifuty0o'):
    print(vowel)

print(list(vowels('Abcedifuty0o')))