data = input().split()

stock = {}

for index in range(0, len(data), 2):
    product_name = data[index]
    quantity = data[index + 1]
    stock[product_name] = int(quantity)


searched_products = input().split()

for product in searched_products:
    quantity = stock.get(product)  # Връща None , ако нямаме такъв ключ 
    if quantity:
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
