square_meters = float(input())
greening = square_meters * 7.61
discount = 0.18 * greening
final_price = greening - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
