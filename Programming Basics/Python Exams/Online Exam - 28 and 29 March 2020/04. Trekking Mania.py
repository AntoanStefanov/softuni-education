number_of_groups = int(input())
total_people = 0
musala = 0  # za %
mont_blanc = 0  # za %
kilimanjaro = 0  # za %
k2 = 0  # za %
everest = 0  # za %

for i in range(1, number_of_groups + 1):
    people_in_one_group = int(input())
    total_people += people_in_one_group

    if people_in_one_group <= 5:
        musala += people_in_one_group
    elif people_in_one_group <= 12:
        mont_blanc += people_in_one_group
    elif people_in_one_group <= 25:
        kilimanjaro += people_in_one_group
    elif people_in_one_group <= 40:
        k2 += people_in_one_group
    elif people_in_one_group >= 41:
        everest += people_in_one_group

p_musala = (musala / total_people) * 100
p_mont_blanc = (mont_blanc / total_people) * 100
p_kilimanjaro = (kilimanjaro / total_people) * 100
p_k2 = (k2 / total_people) * 100
p_everest = (everest / total_people) * 100

print(f"{p_musala:.2f}%")
print(f"{p_mont_blanc:.2f}%")
print(f"{p_kilimanjaro:.2f}%")
print(f"{p_k2:.2f}%")
print(f"{p_everest:.2f}%")
