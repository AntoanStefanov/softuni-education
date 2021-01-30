divisor = int(input())
bound = int(input())
max_num = 0
for num in range(divisor, bound + 1):
    if num % divisor == 0:
        max_num = num

print(max_num)

###### OR #################################


divisor = int(input())
bound = int(input())

max_num = 0
for num in range(bound, 0, -1): # naobratno shtoto tysim nai golqmoto
    if num % divisor == 0:
        print(num)
        break