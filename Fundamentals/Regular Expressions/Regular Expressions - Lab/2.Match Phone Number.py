import re
# pattern = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
# data = input()
# TUPLES () ili ()
# numbers = re.finditer(pattern, data)

# numbers = [number.group(0) for number in numbers]


# print(", ".join(numbers))


# or
# Тук пак е tuple  обаче едното изключва другото за това е в един tuple .
#  Невъзможно е и двете едновременно да са верни
regex = r"(\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4}\b)"

data = input()


phones = re.findall(regex, data)

print(", ". join(phones))
