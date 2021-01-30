
num = (input())

list_num = list(num)
list_num.sort()
list_num.reverse()
res = ''
for i in list_num:
    res += i

print(res)

print("Have a nice day!")