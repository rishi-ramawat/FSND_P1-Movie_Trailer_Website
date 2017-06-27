import webbrowser
import requests
import settings
from typing import List


class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, name: str, genres: List):
        """Constructor of this class

            Args:
                name (str): The Name/Title of the Movie.
                genres (:obj:`list` of :obj:`str`): List of Genres
                                                    this movie belongs to.
        """
        self.title = name
        self.genres = genres
        self.year = None
        self.rating = None
        self.story_line = None
        self.poster_image_url = None
        self.trailer_youtube_url = None

    def __repr__(self):
        return "<{} Movie {}>".format(", ".join(self.genres), self.title)

    # A named constructor
    @classmethod
    def from_omdb_api(cls, imdb_id: str, trailer_url: str):
        """Fetches the movie data using the OMDb API

            Args:
                imdb_id (str): The id to search for in OMDb API.
                trailer_url (str): The Youtube link to the movie's trailer.

            Returns:
                None:  If the Movie Data is not found (or)
                       there was an error in making a request to OMDb API
                Movie: An instance of :class:`Movie` is returned if the
                       request to OMDb API was successful.
        """
        payload = {
            "apikey": settings.OMDB_API_KEY,
            "i": imdb_id,
            "plot": "short",
            "r": "json"
        }
        response = requests.get(settings.OMDB_API_URL, params=payload)

        if (response.ok is not True):
            print("Movie Data Not Found for IMDb Id: {}.".format(imdb_id))
            return None

        movie_data = response.json()
        if (movie_data["Response"] != "True"):
            print("Movie Data Not Found for IMDb Id: {}.".format(imdb_id))
            return None

        movie = cls(movie_data["Title"], movie_data["Genre"].split(", "))
        movie.year = movie_data["Year"]
        movie.rating = movie_data["imdbRating"]
        movie.story_line = movie_data["Plot"]
        movie.poster_image_url = movie_data["Poster"]
        movie.trailer_youtube_url = trailer_url

        return movie

    def show_trailor(self):
        """Plays the movie trailer in a web browser"""
        emptyValues = [
            None, False, 'False', 0, '0',
            0.0, '0.0', 'n', 'no', 'f', ''
        ]
        if (self.trailer_youtube_url in emptyValues):
            print("Please set the Youtube Url for the Trailer first!")
            return

        webbrowser.open(self.trailer_youtube_url)
