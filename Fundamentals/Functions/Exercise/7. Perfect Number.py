
# perfect number is a positive integer that is equal to the sum of its positive divisors,
#  excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself),
#  and 1 + 2 + 3 = 6, so 6 is a perfect number.


number = int(input())


def number_divisors(number):
    divisors = []
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors


def is_perfect(number):
    devisors_sum = sum(number_divisors(number))
    if devisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


res = is_perfect(number)

print(res)
