easter_cakes = int(input())
eggs = int(input())  # 4.35 лв. за кора с 12 яйца
cookies_in_kg = float(input())


easter_cakes_price = easter_cakes * 3.20
eggs_price = eggs * 4.35  # Цена за яйца: 2 кори * 4.35 = 8.70
cookies_in_kg_price = cookies_in_kg * 5.40
eggs_paint_price = eggs * 12 * 0.15


total_price = easter_cakes_price + eggs_price + \
    cookies_in_kg_price + eggs_paint_price

print(f"{total_price:.2f}")
