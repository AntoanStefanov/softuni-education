population = [int(num) for num in input().split(", ")]
wealth_border = int(input())

for num in population:

    max_wealth = max(population)
    max_index = population.index(max_wealth)

    min_wealth = min(population)
    min_index = population.index(min_wealth)

    if min_wealth < wealth_border:
        difference = wealth_border - min_wealth

        if not max_wealth - difference < wealth_border:
            population[max_index] -= difference
            population[min_index] += difference

is_equal = True
for num in population:
    if num < wealth_border:
        is_equal = False
        break

if is_equal:
    print(population)
else:
    print("No equal distribution possible")
