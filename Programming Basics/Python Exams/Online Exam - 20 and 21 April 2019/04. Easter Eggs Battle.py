# 1.	Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# 2.	Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
# След това до получаване на команда "End of battle" се четe многократно един ред:
# 3.	Победител - текст - "one" или "two"


first_player_eggs = int(input())
second_player_eggs = int(input())


command = input()

while command != "End of battle":
    winner = command

    if winner == "one":
        second_player_eggs -= 1
        if second_player_eggs == 0:
            print(
                f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
            break
    elif winner == "two":
        first_player_eggs -= 1
        if first_player_eggs == 0:
            print(
                f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
            break

    command = input()


if command == "End of battle":
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
