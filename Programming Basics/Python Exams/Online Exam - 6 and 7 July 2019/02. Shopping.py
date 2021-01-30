# 1.	Бюджетът на Петър - реално число в интервала [0.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [0…100]
# 3.	Броят процесори - цяло число в интервала [0…100]
# 4.	Броят рам памет - цяло число в интервала [0…100]

budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_RAM_memories = int(input())

video_cards_price = number_of_video_cards * 250

processors_price = (video_cards_price * 0.35) * number_of_processors

RAM_memories_price = (video_cards_price * 0.10) * number_of_RAM_memories

total_price = video_cards_price + processors_price + RAM_memories_price

if number_of_video_cards > number_of_processors:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
