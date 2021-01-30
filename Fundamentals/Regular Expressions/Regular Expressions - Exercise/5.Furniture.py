import re

regex = r"(^>>)(?P<product>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"

furniture = []
total_price = 0

while True:
    data = input()
    if data == "Purchase":
        break
    match = re.match(regex, data)
    if match:  # Ако не е мач , връща None. За туй се прави проверка иначе ш гръмне
        obj = match.groupdict()
        furniture.append(obj["product"])
        total_price += float(obj["price"]) * int(obj["quantity"])


print("Bought furniture:")
for product in furniture:
    print(product)
# print("\n".join(furniture))
print(f"Total money spend: {total_price:.2f}")
