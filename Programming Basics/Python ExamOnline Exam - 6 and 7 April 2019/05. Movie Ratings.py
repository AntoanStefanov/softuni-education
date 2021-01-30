number_of_movies = int(input())
highest_movie_rating = 0
highest_movie_rating_name = ""
lowest_movie_rating = 100
lowest_movie_rating_name = ""
total_rating = 0
for movie in range(1, number_of_movies + 1):
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > highest_movie_rating:
        highest_movie_rating = movie_rating
        highest_movie_rating_name = movie_name
    if movie_rating < lowest_movie_rating:
        lowest_movie_rating = movie_rating
        lowest_movie_rating_name = movie_name

    total_rating += movie_rating


print(f"{highest_movie_rating_name} is with highest rating: {highest_movie_rating:.1f}")
print(f"{lowest_movie_rating_name} is with lowest rating: {lowest_movie_rating:.1f}")
print(f"Average rating: {total_rating / number_of_movies:.1f}")
