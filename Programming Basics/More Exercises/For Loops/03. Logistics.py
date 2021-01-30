number_of_goods = int(input())

minibus = 0
truck = 0
train = 0
all_goods_tonnage = 0

for good in range(1, number_of_goods + 1):
    goods_tonnage = int(input())

    if goods_tonnage <= 3:
        minibus += goods_tonnage
    elif goods_tonnage <= 11:
        truck += goods_tonnage
    else:
        train += goods_tonnage

    all_goods_tonnage += goods_tonnage


average_goods_ton_price = (
    (minibus * 200) + (truck * 175) + (train * 120)) / all_goods_tonnage

print(f"{average_goods_ton_price:.2f}")

minibus_percentage = minibus / all_goods_tonnage * 100
truck_percentage = truck / all_goods_tonnage * 100
train_percentage = train / all_goods_tonnage * 100

print(f"{minibus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
