bitcoins = int(input())
yauns = float(input())
comission_rate = float(input())

# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.


leva_from_bitcoins = bitcoins * 1168

dollars = yauns * 0.15

leva_from_dollars = dollars * 1.76

total_leva = leva_from_bitcoins + leva_from_dollars

euro = total_leva / 1.95

commision = (euro * comission_rate) / 100

print(f"{euro-commision:.2f}")
