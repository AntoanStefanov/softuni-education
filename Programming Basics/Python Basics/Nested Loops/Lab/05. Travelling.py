destination = input()
while destination != "End":
    needed_money = float(input())
    budget = 0
    while budget < needed_money:
        saved_money = float(input())
        budget += saved_money
    print(f"Going to {destination}!")
    destination = input()
