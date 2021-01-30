cake_size = int(input()) * int(input())  # length * width

command = input()
all_pieces = 0

while command != "STOP":
    pieces = int(command)
    all_pieces += pieces
    if all_pieces > cake_size:
        print(
            f"No more cake left! You need {all_pieces - cake_size} pieces more.")
        break
    command = input()
else:
    print(f"{cake_size - all_pieces} pieces are left.")
########### OR #########


cake_width = int(input())
cake_length = int(input())

cake_size = cake_width * cake_length

line = input()
total_pieces = 0
while line != "STOP":  # Когато условието стане False , тоест line == "STOP" ,  тогава се изпълнява else след цикъла, тоест цикълът приключва без ранно прекратяване.
    pieces = int(line)
    total_pieces += pieces
    if total_pieces >= cake_size:
        needed = total_pieces - cake_size
        print(f"No more cake left! You need {needed} pieces more.")
        break

    line = input()
else:

    print(f"{cake_size - total_pieces} pieces are left.")
