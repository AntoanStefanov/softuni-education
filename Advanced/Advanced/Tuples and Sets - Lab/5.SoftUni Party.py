# Може да се реши с един сет с всички гости, при сортирането на стрингове,
#  тези които започват с цифри ще са първи,
#  а вип гостите почват с вифра и се иска те да са първи
regular_guests = set()
vip_guests = set()

num_of_guests = int(input())

for n in range(num_of_guests):
    guest = input()

    if len(guest) == 8:

        if guest[0].isdigit():
            vip_guests.add(guest)
        else:
            regular_guests.add(guest)

vip_guests_who_came = set()
regular_guests_who_came = set()

while True:
    guest = input()
    if guest == "END":
        break
    # Минава и без да проверяваме дали госта съществува в някои от сетовете с резервации
    if guest in regular_guests or guest in vip_guests:
        if guest[0].isdigit():
            vip_guests_who_came.add(guest)
        else:
            regular_guests_who_came.add(guest)


missing_vip_guests = vip_guests - vip_guests_who_came
missing_regular_guests = regular_guests - regular_guests_who_came
all_missing_guests = len(missing_vip_guests | missing_regular_guests)

print(all_missing_guests)
sorted_missing_vip_guests = sorted(missing_vip_guests)  # sorted return a list
sorted_missing_regular_guests = sorted(missing_regular_guests)

for vip_guest in sorted_missing_vip_guests:
    print(vip_guest)
for regular_guest in sorted_missing_regular_guests:
    print(regular_guest)
