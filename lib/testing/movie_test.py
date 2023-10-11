import pytest

from classes.many_to_many import Movie
from classes.many_to_many import Review
from classes.many_to_many import Viewer

class TestMovie:
    '''Movie in many_to_many.py'''

    def test_has_title(self):
        '''Movie is initialized with a title'''
        movie = Movie("Avatar: The Way of Water")
        assert movie.title == "Avatar: The Way of Water"

    def test_title_is_mutable_string(self):
        '''title must be of type string and can change'''
        movie = Movie("Avatar: The Way of Water")
        movie.title = "Avatar: The Way of Ice"
        
        assert movie.title == "Avatar: The Way of Ice"
        assert isinstance(movie.title, str)
        
        # comment out the next two lines if using Exceptions
        # movie.title = 2
        # assert movie.title == "Avatar: The Way of Ice"
        
        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            movie.title = 2

    def test_title_length(self):
        '''title must be longer than 0 characters'''
        movie = Movie("Avatar: The Way of Water")
        
        # comment out the next two lines if using Exceptions
        # movie.title = ""
        # assert movie.title == "Avatar: The Way of Water"
        
        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            movie.title = ""
        
        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Movie("")
    
    def test_has_reviews(self):
        '''movie has a list of reviews'''
        movie_1 = Movie("Scarface")
        movie_2 = Movie("Rashomon")
        viewer = Viewer("Jeffrey")
        review_1 = Review(viewer, movie_1, 1)
        review_2 = Review(viewer, movie_1, 2)
        review_3 = Review(viewer, movie_2, 3)
        
        assert review_1 in movie_1.reviews()
        assert review_2 in movie_1.reviews()
        assert review_3 not in movie_1.reviews()
        assert review_3 in movie_2.reviews()

    def test_reviews_of_type_review(self):
        """movie reviews are of type Review"""
        viewer_1 = Viewer("fabio_the_hmstr")
        movie = Movie("The Bourne Ultimatum")
        Review(viewer_1, movie, 4)
        Review(viewer_1, movie, 5)
        
        assert isinstance(movie.reviews()[0], Review)
        assert isinstance(movie.reviews()[1], Review)

    def test_has_reviewers(self):
        '''movie has a list of reviewers'''
        movie = Movie("Chungking Express")
        viewer_1 = Viewer("William")
        viewer_2 = Viewer("Jeffrey")
        viewer_3 = Viewer("Katherine")
        Review(viewer_1, movie, 3)
        Review(viewer_2, movie, 4)

        assert viewer_1 in movie.reviewers()
        assert viewer_2 in movie.reviewers()
        assert viewer_3 not in movie.reviewers()

    def test_reviewers_of_type_viewer(self):
        """reviewers are of type Viewer"""
        movie = Movie("Chungking Express")
        viewer_1 = Viewer("William")
        viewer_2 = Viewer("Jeffrey")
        Review(viewer_1, movie, 3)
        Review(viewer_2, movie, 4)
        
        assert isinstance(movie.reviewers()[0], Viewer)
        assert isinstance(movie.reviewers()[1], Viewer)
    
    def test_reviewers_are_unique(self):
        """movie reviewers are unique"""
        movie = Movie("Chungking Express")
        viewer_1 = Viewer("William")
        viewer_2 = Viewer("Jeffrey")
        Review(viewer_1, movie, 3)
        Review(viewer_2, movie, 4)
        Review(viewer_1, movie, 5)
        
        assert len(set(movie.reviewers())) == len(movie.reviewers())
        assert len(movie.reviewers()) == 2
        assert viewer_1 in movie.reviewers()
        assert viewer_2 in movie.reviewers()

    def test_calculates_average_rating(self):
        '''calculates and returns the average of its review ratings'''
        movie = Movie("My Neighbor Totoro")
        Review.all = []

        assert movie.average_rating() is None

        Review(viewer=Viewer("username1"), movie=movie, rating=1)
        Review(viewer=Viewer("username2"), movie=movie, rating=3)
        Review(viewer=Viewer("username3"), movie=movie, rating=2)
        Review(viewer=Viewer("username4"), movie=movie, rating=4)
        Review(viewer=Viewer("username5"), movie=movie, rating=5)
        Review(viewer=Viewer("username6"), movie=movie, rating=4)
        Review(viewer=Viewer("username7"), movie=movie, rating=2)
        Review(viewer=Viewer("username8"), movie=movie, rating=3)
        Review(viewer=Viewer("username9"), movie=movie, rating=4)

        assert movie.average_rating() == 3.1
        
        Review.all = []

    # def test_shows_highest_rated(self):
    #     '''returns the highest rated movie'''
    #     Review.all = []
    #     movie_1 = Movie("Avatar: The Way of Water")
    #     movie_2 = Movie("Scarface")
    #     movie_3 = Movie("Rashomon")
    #     movie_4 = Movie("My Neighbor Totoro")
    #     viewer_1 = Viewer("Katherine")
    #     viewer_2 = Viewer("Catherine")
    #     viewer_3 = Viewer("Kathryn")
    #     Review(viewer_1, movie_1, rating=1)
    #     Review(viewer_2, movie_1, rating=3)
    #     Review(viewer_3, movie_1, rating=2)
    #     Review(viewer_1, movie_2, rating=4)
    #     Review(viewer_2, movie_2, rating=5)
    #     Review(viewer_1, movie_3, rating=5)
    #     Review(viewer_2, movie_3, rating=5)
    #     Review(viewer_3, movie_4, rating=3)

    #     assert Movie.highest_rated() == movie_3
    #     assert Movie.highest_rated().title == "Rashomon"

    #     Review.all = []
    #     assert Movie.highest_rated() is None