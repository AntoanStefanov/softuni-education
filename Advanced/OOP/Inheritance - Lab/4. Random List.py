from random import choice
from random import randint
# randint:
# Return random integer in range [a, b], including both end points.

# КАК JUDGE дава 100/100 като идеята на random el е да даде различен елемент ?


class RandomList(list):
    # Тук защо няма
    # def __init__(self, l):
        # self.l = l ?

    def get_random_element(self):
        # -1 bcs both values are included
        element_index = randint(0, len(self) - 1)
        return self.pop(element_index)


random_list = RandomList([1, 2, 3, 4])
print(random_list)
print(random_list.get_random_element())
print(random_list)

li = RandomList()
li.append(4)
li.append(3)
li.append(5)
print(li.get_random_element())  # 5

li = RandomList()
li.append(6)
li.append(1.3)
li.append(10)
li.pop()
li.reverse()
print(sum(li))  # 7.3
print(li.get_random_element())  # 6


# SECOND WAY #


class RandomList(list):
    # Тук защо не е необходимо
    # def __init__(self, l):
        # self.l = l ?

    def get_random_element(self):
        element = choice(self)
        self.remove(element)
        return element
