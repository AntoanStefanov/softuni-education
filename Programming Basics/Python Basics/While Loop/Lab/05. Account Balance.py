command = input()
balance = 0
while command != "NoMoreMoney":
    fee = float(command)
    if fee < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {fee:.2f}")
    balance += fee
    command = input()
print(f"Total: {balance:.2f}")
