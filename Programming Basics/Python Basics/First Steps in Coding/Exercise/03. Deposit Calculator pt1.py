deposit = float(input())
term_in_months = int(input())
annual_interest_rate = float(input())
accrued_interest = deposit * (annual_interest_rate/100)
interest_per_month = accrued_interest / 12
total = deposit + (term_in_months * interest_per_month)
print(total)
