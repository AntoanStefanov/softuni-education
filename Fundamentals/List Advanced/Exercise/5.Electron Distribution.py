total_electrons = int(input())
shells = 1
list_of_electrons = []

while total_electrons > 0:
    electrons = 2 * shells ** 2
    if electrons > total_electrons:
        # Добави толкова колкото имаш, в случая колкото електрона са останали
        list_of_electrons.append(total_electrons)
        break
    list_of_electrons.append(electrons)
    total_electrons -= electrons
    shells += 1
print(list_of_electrons)
