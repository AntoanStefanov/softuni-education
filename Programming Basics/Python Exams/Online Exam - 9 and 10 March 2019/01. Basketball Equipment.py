annual_fee_for_basketball_training = int(input())


basketball_sneakers = annual_fee_for_basketball_training * 0.6

basketball_jersey = basketball_sneakers * 0.8

basketball = basketball_jersey * 1/4

basketball_accessories = basketball * 1/5

total = annual_fee_for_basketball_training + basketball_sneakers + \
    basketball_jersey + basketball + basketball_accessories

print(f"{total:.2f}")
