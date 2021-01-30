# happiness_indexes = list(map(int, input().split()))
# improvement_factor = int(input())

# factored_happiness_indexes = list(
#     map(lambda number: number * improvement_factor, happiness_indexes))

# average_happiness = sum(factored_happiness_indexes) / len(happiness_indexes)

# happy_values = list(filter(
#     lambda employee_happiness: employee_happiness >= average_happiness, factored_happiness_indexes))

# if len(happy_values) >= len(happiness_indexes) / 2:
#     print(
#         f"Score: {len(happy_values)}/{len(happiness_indexes)}. Employees are happy!")
# else:
#     print(
#         f"Score: {len(happy_values)}/{len(happiness_indexes)}. Employees are not happy!")

items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

prices = []

for item in items:
    prices.append(item[1])
print(items)
print(prices)

