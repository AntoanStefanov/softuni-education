from math import ceil
series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
free_time = break_duration / 4
left_time = break_duration - lunch_time - free_time
if left_time >= episode_duration:
    print(
        f"You have enough time to watch {series_name} and left with {ceil(left_time-episode_duration)} minutes free time.")
else:
    print(
        f"You don't have enough time to watch {series_name}, you need {ceil(episode_duration-left_time)} more minutes.")
