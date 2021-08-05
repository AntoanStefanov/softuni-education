
# The way for  iterating through an object unlimited times.
class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self.iterator(self)

    class iterator:
        def __init__(self, reverse_iter_obj):
            self.list_of_numbers = list(reverse_iter_obj.iterable)
            self.index = len(self.list_of_numbers)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration()
            self.index -= 1
            value = self.list_of_numbers[self.index]
            return value



revrse_iterable = reverse_iter([1, 2, 3, 4])
for item in revrse_iterable:
    print(item)

for item in revrse_iterable:
    print(item)




# 100/100 Judge

# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = len(iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration()
#         self.index -= 1
#         value = self.iterable[self.index]
#         return value

# ll = [1, 2, 3, 4, 5]
#
# ll_iter = iter(ll) # pravq go iterable
# print(next(ll_iter))
