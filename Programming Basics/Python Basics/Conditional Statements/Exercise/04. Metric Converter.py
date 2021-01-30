number = float(input())
input_unit_of_measure = input()
output_unit_of_measure = input()

if input_unit_of_measure == "mm" and output_unit_of_measure == "m":
    number *= 0.001
    print(f"{number:.3f}")
if input_unit_of_measure == "mm" and output_unit_of_measure == "cm":
    number *= 0.1
    print(f"{number:.3f}")

if input_unit_of_measure == "cm" and output_unit_of_measure == "m":
    number *= 0.01
    print(f"{number:.3f}")
if input_unit_of_measure == "cm" and output_unit_of_measure == "mm":
    number *= 10
    print(f"{number:.3f}")

if input_unit_of_measure == "m" and output_unit_of_measure == "cm":
    number *= 100
    print(f"{number:.3f}")
if input_unit_of_measure == "m" and output_unit_of_measure == "mm":
    number *= 1000
    print(f"{number:.3f}")
