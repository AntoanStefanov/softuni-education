movie_name = input()
movies_limit = 7
movies = 0
best_movie_points = 0
best_movie = ""

while movie_name != "STOP":  # До команда "STOP" получавате заглавия на любими ваши филми
    movie_points = 0
    for char in movie_name:
        if 65 <= ord(char) <= 90:
            movie_points += ord(char) - len(movie_name)
        elif 97 <= ord(char) <= 122:
            movie_points += ord(char) - (2 * len(movie_name))
        else:
            movie_points += ord(char)
    movies += 1
    if movie_points > best_movie_points:
        best_movie_points = movie_points
        best_movie = movie_name
    if movies == movies_limit:
        print("The limit is reached.")
        break
    movie_name = input()

print(
    f"The best movie for you is {best_movie} with {best_movie_points} ASCII sum.")
