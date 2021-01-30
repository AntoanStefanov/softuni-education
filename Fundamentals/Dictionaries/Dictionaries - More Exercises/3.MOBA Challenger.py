players = {}
total_player_skill = {}

while True:
    data = input()

    if data == "Season end":
        break

    if not 'vs' in data:
        player, position, skill = data.split(" -> ")
        skill = int(skill)
        if player not in players.keys():
            players[player] = [[position, skill]]
        else:
            first_occurance = True
            for info in players[player]:
                if position == info[0]:
                    first_occurance = False
                    if skill > info[1]:
                        info[1] = skill
                        break
            if first_occurance:
                players[player].append([position, skill])
    else:

        player_1, player_2 = data.split(" vs ")
        if player_1 in players.keys() and player_2 in players.keys():
            duel = False
            for info_1 in players[player_1]:
                for info_2 in players[player_2]:
                    if info_1[0] == info_2[0]:
                        if info_1[1] > info_2[1]:
                            del players[player_2]
                            duel = True
                            break
                        else:
                            del players[player_1]
                            duel = True
                            break
                if duel:
                    break


for player, info in players.items():

    total_player_points = 0
    for position, skill in players[player]:
        total_player_points += skill

    total_player_skill[player] = total_player_points


total_player_skill = dict(
    sorted(total_player_skill.items(), key=lambda t: (-t[1], t[0])))

for player1, skill in total_player_skill.items():
    print(f'{player1}: {skill} skill')

    for player2, info in players.items():
        if player1 != player2:
            continue
        info = sorted(info, key=lambda t: (-t[1], t[0]))
        for position, skill in info:
            print(f"- {position} <::> {skill}")
