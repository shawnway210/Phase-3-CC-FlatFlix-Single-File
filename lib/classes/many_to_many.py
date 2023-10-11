class Movie:
    def __init__(self, title):
        self.title = title

    def reviews(self):
        pass

    def reviewers(self):
        pass

    def average_rating(self):
        pass
    
class Review:
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        
class Viewer:
    def __init__(self, username):
        self.username = username

    def reviews(self):
        pass

    def reviewed_movies(self):
        pass

    def has_reviewed_movie(self, movie):
        pass

    def add_review(self, movie, rating):
        pass