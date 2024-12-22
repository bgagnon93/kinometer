import os
from os.path import dirname, abspath
from the_movie_db import TheMovieDb


class Media:
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year
        self.save_path = f"{dirname(abspath(__file__))}/../../public/assets/movies/{title} ({release_year})"
        self.load_media_db()

    def load_media_db(self):
        self.media_db: TheMovieDb = TheMovieDb()
        
    def load_media(self):
        media_data = self.media_db.search_media(self.title, self.release_year)
        media_image_links = self.media_db.get_media_image_links(media_data["id"])
        
        # Filter out backdrops with language (the logo will overlay them). Save only the top 10. 
        backdrops_without_logos = [backdrop for backdrop in media_image_links["backdrops"] if backdrop["iso_639_1"] == None]
        self.save_backdrops(backdrops_without_logos[:10])
        
        # Filter for english language logos only that are in the .png format. Save only the top 10. 
        english_logos = [logo for logo in media_image_links["logos"] if logo["iso_639_1"] == "en" and logo["file_path"].endswith(".png")]
        self.save_logos(english_logos[:10])

        # Filter for english language posters. Logos will not be used when highlighting posters. Save only top 10. 
        english_posters = [poster for poster in media_image_links["posters"] if poster["iso_639_1"] == "en"]
        self.save_posters(english_posters[:10])

    def save_backdrops(self, backdrops):
        for i in range(0, len(backdrops)):
            self.save_image(backdrops[i], f"backdrop{i}", f"{self.save_path}/backdrops")

    def save_logos(self, logos):
        for i in range(0, len(logos)):
            self.save_image(logos[i], f"logo{i}", f"{self.save_path}/logos")

    def save_posters(self, posters):
        for i in range(0, len(posters)):
            self.save_image(posters[i], f"poster{i}", f"{self.save_path}/posters")

    def save_image(self, image_detail, image_name, save_path=None):
        save_path = self.save_path if save_path is None else save_path
        image_link = image_detail["file_path"]
        image = self.media_db.get_media_image(image_link)
        file_name = f"{image_name}.{image_link.split('.')[-1]}"
        file_path = os.path.join(save_path, file_name)
        os.makedirs(save_path, exist_ok=True)
        with open(file_path, "wb") as file:
            file.write(image.content)
        print(f"Image successfully downloaded: {file_path}")
