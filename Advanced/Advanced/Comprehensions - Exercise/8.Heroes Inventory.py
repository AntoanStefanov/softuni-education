heroes = {name: {'items': [], 'cost': 0} for name in input().split(', ')}
while True:
    data = input()
    if data == 'End':
        break
    name, item, cost = data.split('-')
    cost = int(cost)

    if item not in heroes[name]['items']:
        heroes[name]['items'].append(item)
        heroes[name]['cost'] += cost

[print(
    f'{hero} -> Items: {len(items_cost_dict["items"])}, Cost: {items_cost_dict["cost"]}')
 for hero, items_cost_dict in heroes.items()]
