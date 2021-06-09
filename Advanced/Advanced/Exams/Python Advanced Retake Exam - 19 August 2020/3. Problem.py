def numbers_searching(*args):
    duplicates = set()
    for number in args:
        if args.count(number) > 1:
            duplicates.add(number)
    duplicates = sorted(list(duplicates))

    min_num = min(args)
    max_num = max(args)
    missing_value = None
    for num in range(min_num, max_num + 1):
        if not num in args:
            missing_value = num
            break
    return [missing_value, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48,
                        45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
