from math import ceil

tennis_racket_price = float(input())
number_of_tennis_rackets = int(input())
number_of_trainers_pair = int(input())

one_trainers_pair_price = tennis_racket_price * 1/6  # чифт маратонки цена

all_trainers_pairs_price = one_trainers_pair_price * number_of_trainers_pair

tenis_rackets_price = tennis_racket_price * number_of_tennis_rackets

other_equipment = (all_trainers_pairs_price + tenis_rackets_price) * 0.20

total_price = all_trainers_pairs_price + tenis_rackets_price + other_equipment

print(f"Price to be paid by Djokovic {int(total_price / 8)}")
print(f"Price to be paid by sponsors {ceil(total_price * 7/8)}")
