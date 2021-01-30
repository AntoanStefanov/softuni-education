sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for sold_game in range(1, sold_games + 1):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_percentage = hearthstone / sold_games
fornite_percentage = fornite / sold_games
overwatch_percentage = overwatch / sold_games
others_percentage = others / sold_games

print(f"Hearthstone - {hearthstone_percentage:.2%}")
print(f"Fornite - {fornite_percentage:.2%}")
print(f"Overwatch - {overwatch_percentage:.2%}")
print(f"Others - {others_percentage:.2%}")
