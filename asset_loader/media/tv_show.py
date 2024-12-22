from media import Media
from the_movie_db import TheTvDb


class TvShow(Media):
    def load_media_db(self):
        self.media_db = TheTvDb()
