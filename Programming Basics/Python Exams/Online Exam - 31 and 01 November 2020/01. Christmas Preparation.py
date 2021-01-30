paper_rows = int(input())
cloth_rows = int(input())
glue_liters = float(input())
discount_percent = int(input())

paper_price = paper_rows * 5.80
cloth_price = cloth_rows * 7.20
glue_price = glue_liters * 1.20

total = paper_price + cloth_price + glue_price

discount = total * (discount_percent / 100)

print(f"{total - discount:.3f}")
