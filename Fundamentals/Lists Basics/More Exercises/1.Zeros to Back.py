array = [int(el) for el in input().split(", ")]
zeros = []
index = 0
while index < len(array):
    if array[index] == 0:
        zeros.append(array[index])
        del array[index]
        continue
    index += 1

array.extend(zeros)

print(array)
