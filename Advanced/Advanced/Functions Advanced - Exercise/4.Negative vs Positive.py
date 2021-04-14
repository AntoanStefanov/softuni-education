nums = [int(x) for x in input().split()]

positives_nums = list(filter(lambda x: x > 0, nums))
negatives_nums = list(filter(lambda x: x < 0, nums))

print(sum(negatives_nums))
print(sum(positives_nums))

if abs(sum(negatives_nums)) > sum(positives_nums):
    print('The negatives are stronger than the positives')
else:
    print("The positives are stronger than the negatives")
