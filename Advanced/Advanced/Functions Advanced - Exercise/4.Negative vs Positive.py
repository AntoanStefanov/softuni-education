nums = [int(x) for x in input().split()]

positives_nums = list(filter(lambda x: x > 0, nums))
negatives_nums = list(filter(lambda x: x < 0, nums))

print(sum(negatives_nums))
print(sum(positives_nums))

if abs(sum(negatives_nums)) > sum(positives_nums):
    print('The negatives are stronger than the positives')
else:
    print("The positives are stronger than the negatives")


############# Second Timee ####

ints = [int(x) for x in input().split()]

negatives = [num for num in ints if num < 0]
positives = [num for num in ints if num > 0]

neg_sum = sum(negatives)
pos_sum = sum(positives)

print(neg_sum)
print(pos_sum)

[print('The negatives are stronger than the positives')
 if abs(neg_sum) > pos_sum else
 print('The positives are stronger than the negatives')]
