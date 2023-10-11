import pytest

from classes.many_to_many import Movie
from classes.many_to_many import Review
from classes.many_to_many import Viewer

class TestViewer:
    """Viewer in many_to_many.py"""

    def test_has_username(self):
        """Viewer is initialized with a username"""
        viewer_1 = Viewer("gustave_the_cat")
        viewer_2 = Viewer("fanny_the_dog")

        assert viewer_1.username == "gustave_the_cat"
        assert viewer_2.username == "fanny_the_dog"

    def test_username_is_mutable_string(self):
        """username is a mutable string"""
        viewer = Viewer("gustave_the_cat")
        viewer.username = "fanny_the_dog"

        assert viewer.username == "fanny_the_dog"
        assert isinstance(viewer.username, str)

        # comment out the next two lines if using Exceptions
        # viewer.username = 2
        # assert viewer.username == "fanny_the_dog"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            viewer.username = 2

    def test_username_length(self):
        """usernames must be between 6 and 16 characters, inclusive"""
        viewer = Viewer("gustave_the_cat")
        
        # comment out the next two lines if using Exceptions
        # viewer.username = "abcdefghijklmnopq"
        # assert viewer.username == "gustave_the_cat"

        # comment out the next two lines if using Exceptions
        # viewer.username = "abcde"
        # assert viewer.username == "gustave_the_cat"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Viewer("abcde")

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Viewer("abcdefghijklmnopq")

    def test_has_reviews(self):
        """viewer has a list of all reviews submitted"""
        viewer_1 = Viewer("fabio_the_hmstr")
        viewer_2 = Viewer("fanny_the_dog")
        movie = Movie("The Bourne Ultimatum")
        review_1 = Review(viewer_1, movie, 4)
        review_2 = Review(viewer_1, movie, 5)
        review_3 = Review(viewer_2, movie, 3)

        assert review_1 in viewer_1.reviews()
        assert review_2 in viewer_1.reviews()
        assert review_3 not in viewer_1.reviews()
        assert review_3 in viewer_2.reviews()

    def test_reviews_of_type_review(self):
        """viewer reviews are of type Review"""
        viewer_1 = Viewer("fabio_the_hmstr")
        movie = Movie("The Bourne Ultimatum")
        Review(viewer_1, movie, 4)
        Review(viewer_1, movie, 5)

        assert isinstance(viewer_1.reviews()[0], Review)
        assert isinstance(viewer_1.reviews()[1], Review)

    def test_has_reviewed_movies(self):
        """viewer has a list of reviewed movies."""
        viewer = Viewer("fanny_the_dog")
        movie_1 = Movie("Bob's Burgers: The Movie")
        movie_2 = Movie("The Simpsons: The Movie")
        Review(viewer, movie_1, 5)
        Review(viewer, movie_2, 3)

        assert movie_1 in viewer.reviewed_movies()
        assert movie_2 in viewer.reviewed_movies()

    def test_movies_of_type_movie(self):
        """viewer reviewed movies are of type Movie"""
        viewer = Viewer("fanny_the_dog")
        movie_1 = Movie("Bob's Burgers: The Movie")
        movie_2 = Movie("The Simpsons: The Movie")
        Review(viewer, movie_1, 5)
        Review(viewer, movie_2, 3)

        assert isinstance(viewer.reviewed_movies()[0], Movie)
        assert isinstance(viewer.reviewed_movies()[1], Movie)

    def test_reviewed_movies_are_unique(self):
        """viewer reviewed movies are unique"""
        viewer = Viewer("fanny_the_dog")
        movie_1 = Movie("Bob's Burgers: The Movie")
        movie_2 = Movie("The Simpsons: The Movie")
        Review(viewer, movie_1, 5)
        Review(viewer, movie_2, 3)
        Review(viewer, movie_1, 5)

        assert len(set(viewer.reviewed_movies())) == len(viewer.reviewed_movies())
        assert len(viewer.reviewed_movies()) == 2
        assert movie_1 in viewer.reviewed_movies()
        assert movie_2 in viewer.reviewed_movies()

    def test_has_reviewed_movie(self):
        """checks if a movie has been reviewed or not"""
        viewer = Viewer("lucky_the_cat")
        movie_1 = Movie("No Country for Old Men")
        movie_2 = Movie("The Big Lebowski")
        Review(viewer, movie_1, 5)

        assert viewer.has_reviewed_movie(movie_1) == True
        assert viewer.has_reviewed_movie(movie_2) == False

    def test_add_review(self):
        """adds and returns a new review given a movie and a rating"""
        viewer = Viewer("fanny_the_dog")
        movie_1 = Movie("Bob's Burgers: The Movie")
        movie_2 = Movie("The Simpsons: The Movie")
        review_1 = viewer.add_review(movie_1, 5)
        review_2 = viewer.add_review(movie_2, 3)

        assert review_1 in viewer.reviews()
        assert review_2 in viewer.reviews()
        assert isinstance(review_1, Review)
        assert isinstance(review_2, Review)
        assert review_1.movie == movie_1
        assert review_2.movie == movie_2
        assert movie_1 in viewer.reviewed_movies()
        assert movie_2 in viewer.reviewed_movies()

    # def test_reviewer(self):
    #     """returns the viewer who has the most reviews"""
    #     Review.all = []
    #     Viewer.all = []
    #     assert Viewer.top_reviewer() is None
        
    #     viewer_1 = Viewer("fabio_the_hmstr")
    #     viewer_2 = Viewer("fanny_the_dog")
    #     movie_1 = Movie("The Bourne Ultimatum")
    #     movie_2 = Movie("The Bourne Identity")
    #     assert Viewer.top_reviewer() is None
        
    #     Review(viewer_1, movie_1, 4)
    #     Review(viewer_1, movie_2, 2)
    #     Review(viewer_1, movie_1, 1)
    #     Review(viewer_2, movie_1, 3)
    #     Review(viewer_2, movie_1, 5)

    #     assert Viewer.top_reviewer() == viewer_1