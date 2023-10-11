# Object Relations Code Challenge - Flatflix

For this challenge, we'll be working with a Movie Review domain, like Netflix.

We have three models: `Viewer`, `Movie`, and `Review`.

A `Movie` has many `Review`s. A `Viewer` has many `Review`s. A `Review` belongs
to a `Viewer` and belongs to a `Movie`.

`Viewer` - `Movie` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory. Then run
`pipenv shell` to jump into the shell.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge is test-driven. You can run `pytest` at any
time to check your work. You'll need to create your own sample instances so that
you can try out your code on your own. Make sure your relationships and methods
work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Movie

- `Movie __init__(self, title)`
  - `Movie` is initialized with a title
- `Movie property title`
  - Returns the movie's title
  - Titles must be of type `str`
  - Titles must be longer than 0 characters
  - Title **can be** changed after the `Movie` is initialized

#### Viewer

- `Viewer __init__(self, username)`
  - `Viewer` is initialized with a username
- `Viewer property username`
  - Returns the viewer's username
  - Usernames must be of type `str`
  - Usernames must be between 6 and 16 characters, inclusive
  - Usernames **can be** changed after the Viewer is initialized

#### Review

- `Review __init__(self, viewer, movie, rating)`
  - `Review` is initialized with a `Viewer` instance, a `Movie` instance, and a
    rating
- `Review property rating`
  - Returns the rating
  - Ratings must be of type `int`
  - Ratings must be between 1 and 5, inclusive
  - Ratings **cannot be** changed after the review is initialized
  - _hint: hasattr()_

### Object Relationship Methods and Properties

#### Review

- `Review property viewer`
  - Returns the viewer object who wrote the review
  - Must be of type `Viewer`
  - Viewers **can be changed** after the review object is initialized
- `Review property movie`
  - Returns the movie that is being reviewed
  - Must be of type `Movie`
  - Movies **can be changed** after the review object is initialized

#### Viewer

- `Viewer reviews()`
  - Returns a list of reviews associated with the `Viewer` instance.
  - Must be of type `Review`
- `Viewer reviewed_movies(self)`
  - Returns a **unique** list of movies reviewed by the `Viewer` instance.
  - Must be of type `Movie`

#### Movie

- `Movie reviews()`
  - Returns a list of reviews associated with the `Movie` instance.
  - Must be of type `Review`
- `Movie reviewers()`
  - Returns a **unique** list of viewers that reviewed the `Movie` instance.
  - Must be of type `Viewer`

### Aggregate and Association Methods

#### Viewer

- `Viewer has_reviewed_movie(movie)`
  - Receives a `Movie` instance as argument
  - Returns `True` if the viewer has reviewed the `Movie` instance provided
  - Returns `False` otherwise
- `Viewer add_review(movie, rating)`
  - Receives a `Movie` instance and a rating integer as arguments
  - Creates and returns a new review associates with the viewer and movie
    provided

#### Movie

- `Movie average_rating()`
  - Returns the average of all ratings for the `Movie` instance.
  - Rounds the result to the first decimal digit
  - Returns `None` if there are no reviews for the `Movie` instance
  - Reminder: you can calculate the average by adding all ratings together and
    dividing by the total number of ratings.

### Bonus: Aggregate and Association Method

- `Movie classmethod highest_rated()`
  - Returns the `Movie` instance with the highest average rating.
  - Returns `None` if there are no reviews
  - Uncomment lines 130-153 in the movie_test file

- `Viewer classmethod top_reviewer()`
  - Returns the `Viewer` instance with the most reviews
  - Returns `None` if there are no reviews
  - Uncomment lines 141-159 in the viewer_test file
  - _hint: will need a way to remember all viewer objects_

### IF NOT RAISING EXCEPTIONS:

- First, **uncomment** the following lines
  - **viewer_test.py**
    - lines 27-28, 39-40, and 43-44
  - **movie_test.py**
    - lines 24-25, 36-37
  - **review_test.py**
    - lines 27-28, 31-32, 49-50, 53-54, 89-90, and 122-123
- Then, **comment out** the following lines in the test files
  - **viewer_test.py**
    - lines 31-32, 47-48, and 51-52
  - **movie_test.py**
    - lines 28-29, 40-41, and 44-45
  - **review_test.py**
    - lines 35-36, 39-40, 57-58, 61-62, 93-94, and 126-127
