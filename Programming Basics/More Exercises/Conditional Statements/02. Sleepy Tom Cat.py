# норма за игра на Том

standard = 30000


holidays = int(input())
working_days = 365 - holidays


play_time = working_days * 63 + holidays * 127


if play_time > standard:
    over_minutes = play_time - standard

    hours = over_minutes // 60
    minutes = over_minutes % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    left_minutes = standard - play_time

    hours = left_minutes // 60
    minutes = left_minutes % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
