pages_in_one_book = int(input())
page_per_hour = int(input())
days_to_read = int(input())
total_reading_time = pages_in_one_book / page_per_hour
required_hours_per_day = total_reading_time / days_to_read
print(required_hours_per_day)
