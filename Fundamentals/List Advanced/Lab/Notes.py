### List Comprehension ###
# Създава нов списък с output стойностите
# Не може с  while loop
numbers = [1, 2, 3, 4, 5]
# Output Expression | x-variable , numbers-input sequence
squares = [x ** 2 for x in numbers]
print(squares)

### List Comprehension, Optinal parameter ###
numbers = [1, 2, 3, 4, 5]
# Output Expression |For Loop Expression (x-variable , numbers-input sequence) | Optional parameter(Conditional expression)
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)


### List Methods ###

# ADDING

# Append method
# Add single element at the end

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Extend method
# Add multiple elements at the end

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

# Insert method
# Add single element at a specific index (index: int, object)

my_list = [1, 2, 3]
my_list.insert(2, 4)
print(my_list)

# REMOVING

# Clear method
# Removes all elements

my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# Pop method
# Removes last element and returns it
# If argument is given , it removes the value ot the given INDEX
my_list = [1, 2, 3]
last = my_list.pop()
print(my_list)
print(last)

# Remove method
# Removes by value (first occurrence)

my_list = [1, 2, 3, 1]
my_list.remove(1)
print(my_list)


### Sorting ###
# Трябва да са int иначе гърми.
# sorted може да сортира и tuples по нулевия индекс , ако те са равни проверява следващите
# и когато срещне разлика , който е по-малък от другия - целият лист става първи .
print(sorted([[1, 2, 4, 4], [1, 2, 3, 4]]))


#### More methods ###

# Count method

my_list = [1, 2, 3, 2, 2]
# Finds all occurrences in a list of an object
numbers_of_two = my_list.count(2)
print(numbers_of_two)


# Index method

my_list = [1, 2, 3, 2, 2]
# Finds the index of the first occurrence in a list of an object
index_of_two = my_list.index(2)
print(index_of_two)

# Reverse method

my_list = [1, 2, 3]
# reverses the elements mutating the list
my_list.reverse()
print(my_list)

# returns new list
x = list(reversed(my_list))
print(x)


### Advanced Methods ###

# Lamba function

# lambda operator is used for creating small , one-time and anonymous function objects in Python

# lambda basic syntax

# lamda x : int(x)
# keyword statement(parameter - не връща стойност a = 1) : expression (връща стойност - word == word[::-1])
# Може след като се присвой да се извика колкото пъти искат
# words = input().split()
# searched_palindrome = input()
# # Вкарване на ламбда функция в comprehension без да се налага да я присвояваме към променлива.
# # Call-ваме lambda функцията с (word) като параметър на функ. Много грозен код за ПАЙТЪН .
# # Не го прави в Пайтън ,В Javascript се прави(iife - Immediately invoked function expression. Дефинирана и извикана веднага)
# palindromes = [word for word in words if (lambda w: w[::-1])(word)]
# print(palindromes)
# print(f"Found palindrome {palindromes.count(searched_palindrome)} times")

# Ламбда се използва за всякъде , на всякъде
# Отдолъ са лабда изрази , след сейф ми ги обръща така .
def a(fn): return fn()


def b(): return 5


print(a(b))


# Map function

# Builtin function

# map(function-само препратка без да я викаме с (), *iterables(Обект, който може да е обходен като лист))
#  -> връща map object(iterator object)
# map(fn, [1,2,3,4,5,6] - последователност, която може да бъде модифицирана)
print(map(lambda n: n + 1, [1, 2, 3, 4, 5, 6]))
# Връща map обекта (специален обект ) при call (неизпълнен)
# обръщане към лист , изпълнява обекта
print(list(map(lambda n: n + 1, [1, 2, 3, 4, 5, 6])))


strings_list = ["1", "2", "3", "4"]
# Връща int(x), за всеки х в iterable-string_list
numbers_list = list(map(lambda x: int(x), strings_list))
print(numbers_list)


def mul_by_two(n):
    return n * 2


# препратка към Функция(без () ) и итеръбъл(лист в случая)
# резултатът от мап фунцкията се каства към лист .
multiplied_list = list(map(mul_by_two, [1, 2, 3]))
print(multiplied_list)


# Горното е същото като
multiplied_list = list(map(lambda n: n * 2, [1, 2, 3]))
print(multiplied_list)


# Filter function
# Builtin function

# filters elements that fulfill a given condition
# filter(function or None, iterable) -> връща filter object(iterator object)
# Приема като първи аргумент функция или None type- обект , и втори аргумент приема някаква колекция , която може да бъде обходена


# Filter си прилича с map, Но може да се подаде филтрираща функция като първи аргумент
# и ако резултатът от изпълнението на тази функция върне True, елементът остава в стойностите,
# които ще бъдат върнати от филтър , ако не елементът бива филтриран(премахнат)

my_list = [-1, 5, -2, 10, -3, 20]
filtered_list = list(filter(lambda n: n > 0, my_list))
print(filtered_list)
# Върна всички положителни числа
# работи като map,  само че map  приема елемент по елемент всички стойности , подава ги на функцията(първия аргумент)
# и всеки един от тези елементи, върната стойност при map - става нова стойност.
# А при FILTER нещата , които не са вярни , няма да останат в нашия израз. Филтрира на база подадена фунцкия.


## Enumerate ###
# Връща обект iterator enumerate обект(неизпълнен), който ако го кастнеме към лист връща лист с обекта tuple(индекс, елемент)
print(enumerate([55, 45, 66, 23, 99]))
print(list(enumerate([55, 45, 66, 23, 99])))


### Additional List Manipulations ###

# Set method

# You can use the set() method to extract only the unique elements from a list

numbers = [1, 2, 2, 3, 1, 4, 5, 4]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]


# Concatenating lists

nums_list_1 = [1, 2, 3]
nums_list_2 = [4, 5, 6]
final_list = nums_list_1 + nums_list_2  # [1, 2, 3, 4, 5, 6]


# Swaping list elements

nums = [1, 2, 3]
nums[0], nums[1], nums[2] = nums[2], nums[0], nums[1]
# 1 swaps with 3
# 2 swaps with 1
# 3 swaps with 2

# list unpacking
nums = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5]

first, second, *others = nums
# first = 1
# second = 2
# other = 3, 4, 4, 4, 4, 4, 4, 5

nums = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5]

first, *others, last = nums

# first  = 1
# others = 2, 3, 4, 4, 4, 4, 4, 4
# last = 5
