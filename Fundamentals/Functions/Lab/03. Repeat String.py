
# Типизация , подсказване за другите читатели
string: str = input()  # Може и тук да се подскаже type hint
repeat_time: int = int(input())  # Може и тук да се подскаже type hint


# type hint Програмистите по лесно ще четат и ориентират кода така
def operation(string: str, repeat_time: int):
    return string * repeat_time


print(operation(string, repeat_time))
