mapper = {"shards": "Shadowmourne",
          "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}

junk = {}

is_found = False

while True:

    data = input().split(" ")

    for index in range(0, len(data), 2):

        quantity = int(data[index])
        material = data[index+1].lower()

        if material in key_materials:

            key_materials[material] += quantity

            if key_materials[material] >= 250:
                print(f"{mapper[material]} obtained!")
                key_materials[material] -= 250
                is_found = True
                break

        else:

            if material not in junk:
                junk[material] = 0

            junk[material] += quantity

    if is_found:
        break


ordered_keys_materials = sorted(
    key_materials.items(), key=lambda x: (-x[1], x[0]))

for item, quantity in ordered_keys_materials:
    print(f"{item}: {quantity}")

ordered_junk = sorted(junk)

for item in ordered_junk:
    print(f"{item}: {junk[item]}")
