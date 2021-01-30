def product_sign(a, b, c):
    nums = [a, b, c]
    zero = False
    negative_signs = 0

    for num in nums:
        if num == 0:
            zero = True
            break
        elif num < 0:
            negative_signs += 1

    if zero:
        return "zero"
    elif negative_signs % 2 == 1:
        return "negative"
    else:
        return "positive"


first_num = float(input())
second_num = float(input())
third_num = float(input())


sign = product_sign(first_num, second_num, third_num)
print(sign)
