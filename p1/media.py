import webbrowser

class Video():
    """ This class provides a way to store video related information """

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class TvShow(Video):
    """ This class provides a way to store tv show related information """

    def __init(self, show_title, show_length, show_season, show_episode,
               tv_station):
        Video.__init__(self, show_title, show_length)
        self.season = show_season
        self.episode = show_episode
        self.station = tv_station

class Movie(Video):
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_length, movie_rating):
        Video.__init__(self, movie_title, movie_length)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        for rating in Movie.VALID_RATINGS:
            if rating == movie_rating:
                self.rating = movie_rating
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
