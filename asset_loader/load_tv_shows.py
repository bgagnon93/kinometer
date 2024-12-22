from os.path import dirname, abspath
from media import TvShow
from utils.load_file import load_json_file_path


def load_tv_shows():
    tv_shows = load_json_file_path(f"{dirname(abspath(__file__))}/data/tv_shows.json")
    for tv_show in tv_shows[0:]:
        TvShow(tv_show["title"], tv_show["releaseYear"]).load_media()


if __name__ == "__main__":
    load_tv_shows()