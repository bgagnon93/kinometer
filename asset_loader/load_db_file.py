import os, json
from os.path import dirname, abspath, join
from utils.load_file import load_json_file_path

def main():
    # load data files into a single media list
    movies = load_json_file_path("./asset_loader/data/movies.json")
    tv_shows = load_json_file_path("./asset_loader/data/tv_shows.json")
    games = load_json_file_path("./asset_loader/data/games.json")
    media_list = movies + tv_shows + games

    # Add paths for backdrops, logos, and posters to each media object. 
    base_path="./public/assets/movies"
    for media in media_list:
        media_path = join(base_path, media["moviePath"])

        # Paths for backdrops, logos, and posters
        backdrops_path = join(media_path, "backdrops")
        logos_path = join(media_path, "logos")
        posters_path = join(media_path, "posters")

        backdrops = build_list_of_files_in_dir(backdrops_path, "backdrop")
        logos = build_list_of_files_in_dir(logos_path, "logo")
        posters = build_list_of_files_in_dir(posters_path, "poster")

        # Update the dictionary
        media["backdrops"] = sorted(backdrops)
        media["logos"] = sorted(logos)
        media["posters"] = sorted(posters)

    # Write the file to movies.js data store
    media_list_app_data = json.dumps(media_list, indent=2)
    with open("./src/data/movies.js", "w") as file:
        file.write(f"export default {media_list_app_data};")


def build_list_of_files_in_dir(path, file_prefix=""):
    file_list = []
    if os.path.exists(path):
        for file in os.listdir(path):
            if file.startswith(file_prefix):
                file_list.append(file)
    return file_list

if __name__ == "__main__":
    main()
