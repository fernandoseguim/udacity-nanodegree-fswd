import webbrowser


class Video(object):

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """This class provides a way to store movie related information:
    "title" is the title of the movie
    "storyline" is a summary about the movie
    "poster_image_url" is a url to movie's poster
    "trailer_youtube_url" is a url to movie's trailer on youtube """

    def __init__(self, title, duration, storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        try:
            webbrowser.open(self.trailer_youtube_url)
        except ModuleNotFoundError as error:
            print(error)


class TVShow(Video):

    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        pass