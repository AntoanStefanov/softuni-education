series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_duration_without_ads = float(input())

ads_for_episode = episode_duration_without_ads * 0.20

episode_duration_with_ads = ads_for_episode + episode_duration_without_ads

extra_duration_from_special_episodes = number_of_seasons * 10

total_watch_time = episode_duration_with_ads * number_of_episodes * \
    number_of_seasons + extra_duration_from_special_episodes
print(
    f"Total time needed to watch the {series_name} series is {int(total_watch_time)} minutes.")
