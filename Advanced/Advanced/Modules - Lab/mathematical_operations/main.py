from mapper import operator_mapper

num_1, operator, num_2 = input().split()

num_1 = float(num_1)
num_2 = int(num_2)

print(operator_mapper[operator](num_1, num_2))
