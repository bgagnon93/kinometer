from os.path import dirname, abspath
from media import Movie
from utils.load_file import load_json_file_path


def load_movies():
    movies = load_json_file_path(f"{dirname(abspath(__file__))}/data/movies.json")
    for movie in movies[0:]:
        Movie(movie["title"], movie["releaseYear"]).load_media()


if __name__ == "__main__":
    load_movies()