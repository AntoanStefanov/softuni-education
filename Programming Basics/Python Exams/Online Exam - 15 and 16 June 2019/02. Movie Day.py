photos_time = int(input())
number_of_scenes = int(input())
scene_duration = int(input())

preperation = photos_time * 15 / 100

needed_time_for_scenes = number_of_scenes * scene_duration

total_needed_time = needed_time_for_scenes + preperation
difference = abs(photos_time - total_needed_time)
if photos_time >= total_needed_time:
    print(
        f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(
        f"Time is up! To complete the movie you need {round(difference)} minutes.")
