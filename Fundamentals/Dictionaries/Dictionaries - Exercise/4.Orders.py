# w/ 2 dictionaries
# products_price = {}
# products_quantities = {}


# while True:
#     data = input()

#     if data == "buy":
#         break

#     product, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)

#     if product not in products_price:
#         products_price[product] = 0
#         products_quantities[product] = 0
#     products_price[product] = price
#     products_quantities[product] += quantity


# for product, price in products_price.items():
#     total_for_product = price * products_quantities[product]
#     print(f"{product} -> {total_for_product:.2f}")

# w/ nested dictionaries

products = {}


while True:
    data = input()

    if data == "buy":
        break

    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {"price": 0, "quantity": 0}
    products[product]["price"] = price
    products[product]["quantity"] += quantity


for product, price_quantity_data in products.items():
    total_for_product = price_quantity_data["price"] * \
        price_quantity_data["quantity"]

    print(f"{product} -> {total_for_product:.2f}")


# with lists

orders = {}


while True:
    data = input()
    if data == "buy":
        break

    name, price, quantity = data.split()

    if name not in orders:
        orders[name] = [float(price), int(quantity)]
    else:
        list_of_name = orders[name]
        list_of_name[0] = float(price)
        list_of_name[1] += int(quantity)

for item in orders.items():
    list_of_price_and_quantity = item[1]
    print(
        f"{item[0]} ->{list_of_price_and_quantity[0] * list_of_price_and_quantity[1]: .2f}")
