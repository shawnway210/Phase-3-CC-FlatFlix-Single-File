class Movie:
    def __init__(self, title):
        self.title = title

        self._reviews = []
        self._viewers = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception("The title must be asrting and name must have more than 0 characters")
    
    def reviews(self):
        return self._reviews
        pass

    def reviewers(self):
        return list(set(self._viewers))
        pass

    def average_rating(self):
        if self._reviews:
            average = sum([review.rating for review in self._reviews]) / len(self._reviews)
            return round(average, 1) 
        else:
            return None
        pass
    
class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        Review.all.append(self)

        self.movie._reviews.append(self)
        self.movie._viewers.append(self.viewer)

        self.viewer._reviews.append(self)
        self.viewer._movies.append(movie)


    
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("The viewer must be an instance of Viewer")
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("The movie must be an instance of Movie")

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 1 <= round(rating) <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else:
            raise Exception("The rating must be an interger and between 1 and 5")
               
class Viewer:
    def __init__(self, username):
        self.username = username

        self._reviews = []
        self._movies = []
   
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("The username must be srtin g and between 6 and 16 characters")

    def reviews(self):
        return self._reviews
        pass

    def reviewed_movies(self):
        return list(set(self._movies))
        pass

    def has_reviewed_movie(self, movie):
        if movie in self._movies:
            return True 
        else:
            return False
        pass

    def add_review(self, movie, rating):
        return Review(self, movie, rating)
        pass