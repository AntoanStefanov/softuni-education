import re


regex = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"


n = int(input())

for _ in range(n):
    barcode = input()

    match = re.match(regex, barcode)
    if match:
        valid_barcode = match.group()
        product_group = ''
        for char in valid_barcode:
            if char.isdigit():
                product_group += char
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
