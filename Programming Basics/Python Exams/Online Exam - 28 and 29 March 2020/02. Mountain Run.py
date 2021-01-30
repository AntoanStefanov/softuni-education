record = float(input())
distance = float(input())
seconds_for_meter = float(input())


seconds = distance * seconds_for_meter


delay = int(distance / 50) * 30


total_seconds = seconds + delay


if total_seconds >= record:
    print(f"No! He was {total_seconds - record:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_seconds:.2f} seconds.")
