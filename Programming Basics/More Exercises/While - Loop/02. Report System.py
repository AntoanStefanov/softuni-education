expected_saved_money = int(input())


command = input()
transaction_number = 1
total_saved = 0
cash = 0
card = 0
cash_transaction = 0
card_transaction = 0
while command != "End":

    money_transaction = int(command)

    if transaction_number % 2 == 1:  # Cash
        if money_transaction > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_saved += money_transaction
            cash += money_transaction
            cash_transaction += 1

    elif transaction_number % 2 == 0:  # Card
        if money_transaction < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_saved += money_transaction
            card += money_transaction
            card_transaction += 1

    if total_saved >= expected_saved_money:
        break
    transaction_number += 1
    command = input()

if total_saved >= expected_saved_money:
    print(f"Average CS: {cash / cash_transaction:.2f}")
    print(f"Average CC: {card / card_transaction:.2f}")
else:
    print("Failed to collect required money for charity.")
