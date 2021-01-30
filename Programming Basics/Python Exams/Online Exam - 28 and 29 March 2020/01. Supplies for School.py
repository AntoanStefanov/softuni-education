package_pens = int(input())
package_markers = int(input())
liters_liquid = float(input())
discount = int(input())

package_pens_price = package_pens * 5.80
package_markers_price = package_markers * 7.20
liquid_price = liters_liquid * 1.20

total_price = package_pens_price + package_markers_price + liquid_price

total_price -= total_price * discount / 100
print(f"{total_price:.3f}")
