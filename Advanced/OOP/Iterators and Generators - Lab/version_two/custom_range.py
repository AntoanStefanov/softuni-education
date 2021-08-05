# Правилен начин, правим допълнителен клас, който представлява само итератора на нашия обект
# (Иначе при два фор-а не върви)
# TAKA PRI VSQKO VURTENE SHTE RABOTI < NE samo za edin for cikul
# N na broi iteratora za edin i sushti obekt.
class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.iterator(self)

    def __reversed__(self):  # ZA da moje da go reversnem kogato se vikne obekta s reversed()
        return self.iterator(self, is_reversed=True)

    class iterator:

        def __init__(self, custom_range_obj, is_reversed=False):
            self.custom_range_obj = custom_range_obj
            self.is_reversed = is_reversed
            if self.is_reversed:
                self.value = self.custom_range_obj.end
            else:
                self.value = self.custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value < self.custom_range_obj.start or self.value > self.custom_range_obj.end:
                raise StopIteration()

            value = self.value
            if self.is_reversed:
                self.value -= 1
            else:
                self.value += 1
            return value

    # # PRI REVERSED(custom_range) FUNCKIUqta SE VIKA __reversed__
    # class reversed_iterator:
    #     def __init__(self, custom_range_obj):
    #         self.custom_range_obj = custom_range_obj
    #         self.value = self.custom_range_obj.end
    #
    #     def __iter__(self):
    #         return self
    #
    #     def __next__(self):
    #         if self.value < self.custom_range_obj.start:
    #             raise StopIteration()
    #         value = self.value
    #         self.value -= 1
    #         return value


one_to_ten = custom_range(1, 10)
print(one_to_ten)
for num in one_to_ten:
    print(num)

for num in one_to_ten:
    print(num)

for num in reversed(one_to_ten):
    print(num)

# Judge 100/100 ##
# class custom_range:
#
#     def __init__(self, s, end):
#         self.current_num = s
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         number = self.current_num
#         self.current_num += 1
#         if number > self.end:
#             raise StopIteration()
#         return number
