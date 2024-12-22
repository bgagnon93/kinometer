import requests


class TheMovieDb:
    search_media_url = "https://api.themoviedb.org/3/search/movie"
    get_media_url = "https://api.themoviedb.org/3/movie"
    get_media_image_url = "https://image.tmdb.org/t/p/original"

    def __init__(self):
        self.TMDB_API_KEY = "" # TODO: Make this secret

    def search_media(self, movie_title, year):
        # Search parameters
        params = {
            "api_key": self.TMDB_API_KEY,
            "query": movie_title,
            "year": year,
        }

        response = requests.get(self.search_media_url, params=params)
        if response.status_code != 200:
            print(f"Error: Unable to fetch movie data for {movie_title}. Status code: {response.status_code}")
            return False

        data = response.json()
        if not data["results"]:
            print(f"No results found for '{movie_title} ({year})'.")
            return False

        # Get the first movie result
        return data["results"][0]
    
    def get_media_image_links(self, movie_id):
        params = {"api_key": self.TMDB_API_KEY}
        response = requests.get(f"{self.get_media_url}/{movie_id}/images", params=params)
        data = response.json()
        return data
    
    def get_media_image(self, image_link):
        params = {"api_key": self.TMDB_API_KEY}
        response = requests.get(f"{self.get_media_image_url}{image_link}", params=params)
        return response
