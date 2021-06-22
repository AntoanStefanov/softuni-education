def stock_availability(boxes: list, action, *args):
    if action == 'delivery':
        boxes.extend(args)
    elif action == 'sell':
        if not args:  # no args
            boxes.pop(0)
        else:
            if type(args[0]) == int:
                sold_boxes = args[0]
                for _ in range(sold_boxes):
                    boxes.pop(0)
            else:
                for flavor in args:
                    while flavor in boxes:
                        boxes.remove(flavor)
    return boxes


print(stock_availability(
    ["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(
    ["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
