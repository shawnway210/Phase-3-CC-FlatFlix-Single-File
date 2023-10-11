import pytest

from classes.many_to_many import Movie
from classes.many_to_many import Review
from classes.many_to_many import Viewer

class TestReview:
    '''Review in many_to_many.py'''

    def test_has_rating(self):
        '''Review is initialized with a rating'''
        movie = Movie("101 Dalmatians")
        viewer = Viewer("pongo_the_dog")
        review_1 = Review(viewer, movie, 5)
        review_2 = Review(viewer, movie, 4)

        assert review_1.rating == 5
        assert review_2.rating == 4

    def test_rating_is_immutable_int(self):
        """ratings are of type int and cannot be changed after initialization"""
        movie = Movie("101 Dalmatians")
        viewer = Viewer("pongo_the_dog")
        review_1 = Review(viewer, movie, 5)
        
        # comment out the next two lines if using Exceptions
        # review_1.rating = 4
        # assert review_1.rating == 5

        # comment out the next two lines if using Exceptions
        # review_1.rating = "three"
        # assert review_1.rating == 5
        
        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            review_1.rating = 4
        
        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Review(viewer, movie, "three")
        
    def test_rating_range(self):
        '''ratings must be between 1 and 5, inclusive.'''
        movie = Movie("Breathless")
        viewer = Viewer("snap_the_turtle")
        review_1 = Review(viewer, movie, 5)
        
        # comment out the next two lines if using Exceptions
        # review_1.rating = 6
        # assert review_1.rating == 5
        
        # comment out the next two lines if using Exceptions
        # review_1.rating = 0
        # assert review_1.rating == 5
        
        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Review(viewer, movie, 6)
        
        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Review(viewer, movie, 0)

    def test_has_a_viewer(self):
        '''review has a viewer'''
        movie = Movie("Breathless")
        viewer_1 = Viewer("snap_the_turtle")
        review_1 = Review(viewer_1, movie, 5)
        review_2 = Review(viewer_1, movie, 4)
        
        assert review_1.viewer == viewer_1
        assert review_2.viewer == viewer_1

    def test_viewer_of_type_viewer_and_mutable(self):
        """viewer is of type Viewer and mutable"""
        movie = Movie("Breathless")
        viewer_1 = Viewer("snap_the_turtle")
        viewer_2 = Viewer("snag_the_snail")
        review_1 = Review(viewer_1, movie, 5)
        review_2 = Review(viewer_1, movie, 4)
        
        assert isinstance(review_1.viewer, Viewer)
        assert isinstance(review_2.viewer, Viewer)
        
        review_1.viewer = viewer_2
        assert review_1.viewer.username == "snag_the_snail"

        #comment out the next two lines if using Exceptions
        # review_1.viewer = "Penny the Dog"
        # assert review_1.viewer.username == "snag_the_snail"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Review("Penny the Dog", movie, 3)

    def test_has_a_movie(self):
        '''review has a movie'''
        movie_1 = Movie("Breathless")
        movie_2 = Movie("The 400 Blows")
        viewer_1 = Viewer("snap_the_turtle")
        review_1 = Review(viewer_1, movie_1, 5)
        review_2 = Review(viewer_1, movie_2, 4)
        
        assert review_1.movie == movie_1
        assert review_2.movie == movie_2

    def test_movie_of_type_movie_and_mutable(self):
        """movie is of type Movie and mutable"""
        movie_1 = Movie("Breathless")
        movie_2 = Movie("The 400 Blows")
        viewer_1 = Viewer("snap_the_turtle")
        review_1 = Review(viewer_1, movie_1, 5)
        review_2 = Review(viewer_1, movie_2, 4)
        
        assert isinstance(review_1.movie, Movie)
        assert isinstance(review_2.movie, Movie)
        
        review_1.movie = movie_2
        assert review_1.movie.title == "The 400 Blows"

        #comment out the next two lines if using Exceptions
        # review_1.movie = "Indianan Jones"
        # assert review_1.movie.title == "The 400 Blows"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Review(viewer_1, "Breathless", 3)

    def test_get_all_reviews(self):
        """Review class has all attribute"""
        Review.all = []
        movie = Movie("Breathless")
        viewer = Viewer("snap_the_turtle")
        review_1 = Review(viewer, movie, 5)
        review_2 = Review(viewer, movie, 4)
        
        assert len(Review.all) == 2
        assert review_1 in Review.all
        assert review_2 in Review.all