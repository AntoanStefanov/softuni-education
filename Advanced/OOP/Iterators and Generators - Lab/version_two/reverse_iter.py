# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass
#
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)

ll = [1, 2, 3, 4, 5]

ll_iter = iter(ll)
print(next(ll_iter))