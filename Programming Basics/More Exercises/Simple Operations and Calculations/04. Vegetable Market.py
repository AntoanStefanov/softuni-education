price_vegetables_kilo = float(input())

price_fruits_kilo = float(input())

kilos_vegetables = int(input())

kilos_fruits = int(input())


price_vegetables = price_vegetables_kilo * kilos_vegetables

price_fruits = price_fruits_kilo * kilos_fruits

total = price_vegetables + price_fruits

euro = total / 1.94

print(f"{euro:.2f}")