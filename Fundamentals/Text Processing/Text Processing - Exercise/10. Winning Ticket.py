tickets = input().split(", ")
winning_symbols = ['@', '#', '$', '^']


def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol * 20 == ticket:
            print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
            return True
    return False


def is_winning_ticket(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for winning_symbol in winning_symbols:
        if winning_symbol * 6 in left_half and winning_symbol * 6 in right_half:
            left_count = left_half.count(winning_symbol)
            right_count = right_half.count(winning_symbol)
            print(
                f'ticket "{ticket}" - {min(left_count, right_count)}{winning_symbol}')
            return True

    return False


for t in tickets:
    ticket = t.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue
    if is_jackpot(ticket):
        continue
    if is_winning_ticket(ticket):
        continue

    print(f'ticket "{ticket}" - no match')
