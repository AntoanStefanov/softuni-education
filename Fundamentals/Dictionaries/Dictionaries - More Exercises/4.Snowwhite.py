dwarfs = {}


while True:
    data = input()
    if data == 'Once upon a time':
        break

    name, hat_color, physics = data.split(' <:> ')
    physics = int(physics)

    if name not in dwarfs.keys():
        dwarfs[name] = [[hat_color, physics]]
    else:
        same_dwarf = False
        for info in dwarfs[name]:
            if info[0] == hat_color:
                same_dwarf = True
                if physics > info[1]:
                    info[1] = physics
                    break

        if not same_dwarf:
            dwarfs[name].append([hat_color, physics])


### Dark India (below) ###

def dict_to_sort(dwarfs):
    colors = {}
    for name, hats in dwarfs.items():
        for color, physics in hats:
            owners = colors.setdefault(color, set())
            owners.add(name)
            yield color, name, physics, owners


def sorted_dict(dwarfs):
    for t in sorted(dict_to_sort(dwarfs), key=lambda t: (t[2], len(t[3])), reverse=True):
        yield t[:3]


for color, name, physics in sorted_dict(dwarfs):
    print(f'({color}) {name} <-> {physics}')


# dwarfs = {}
# while True:
#     data = input()
#     if data == 'Once upon a time':
#         break

#     name, hat_color, physics = data.split(' <:> ')
#     physics = int(physics)

#     if name not in dwarfs.keys():
#         dwarfs[name] = [[hat_color, physics]]
#     else:
#         same_dwarf = False
#         for info in dwarfs[name]:
#             if info[0] == hat_color:
#                 same_dwarf = True
#                 if physics > info[1]:
#                     info[1] = physics
#                     break

#         if not same_dwarf:
#             dwarfs[name].append([hat_color, physics])


# color_count = {}

# for name, info in dwarfs.items():
#     for color, physics in info:
#         if color not in color_count:
#             color_count[color] = 0
#         color_count[color] += 1

# print(dwarfs)
# print(color_count)


# sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: x[1]))


# items = input()
# dwarfs = {}
# colors = {}
# while items != "Once upon a time":
#     tokens = items.split(" <:> ")
#     name = tokens[0]
#     color = tokens[1]
#     physics = int(tokens[2])
#     id = name + ":" + color
#     if id not in dwarfs:
#         if color not in colors:
#             colors[color] = 1
#         else:
#             colors[color] += 1
#         dwarfs[id] = [0, color]
#     dwarfs[id][0] = max([dwarfs[id][0], physics])
#     items = input()

# sorted_dwrafs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))
# for key, value in sorted_dwrafs.items():
#     tokens = key.split(":")
#     print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")