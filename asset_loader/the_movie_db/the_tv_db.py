from .the_movie_db import TheMovieDb

# TheTvDb is still technically TheMovieDb. Endpoints are slightly different. 
class TheTvDb(TheMovieDb):
    search_media_url = "https://api.themoviedb.org/3/search/tv"
    get_media_url = "https://api.themoviedb.org/3/tv"
    get_media_image_url = "https://image.tmdb.org/t/p/original"
