import fresh_tomatoes
import json
import media
import settings


movies = []  # type: List[media.Movie]

if settings.OMDB_API_KEY is not None:  # If you have access to OMDb API
    with open('movies_list_omdb.json', 'r') as file:
        json_data = json.load(file)

    for var in json_data:
        movie = media.Movie.from_omdb_api(
            var["imdb_id"],
            var["trailer_youtube_url"]
        )

        if movie is not None:
            movies.append(movie)

else:  # If you do not have access to OMDb API (As it is a paid API now)

    with open('movies_list.json', 'r') as file:
        json_data = json.load(file)

    for movie_data in json_data:
        movie = media.Movie.from_json(movie_data)
        movies.append(movie)

# Generate & open an HTML page and populate it with all the movies data.
fresh_tomatoes.open_movies_page(movies)
