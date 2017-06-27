import fresh_tomatoes
import json
import media


with open('movies_list_omdb.json', 'r') as file:
    json_data = json.load(file)

movies = []  # type: List[media.Movie]

for var in json_data:
    movie = media.Movie.from_omdb_api(
        var["imdb_id"],
        var["trailer_youtube_url"]
    )

    if movie is not None:
        movies.append(movie)

fresh_tomatoes.open_movies_page(movies)
