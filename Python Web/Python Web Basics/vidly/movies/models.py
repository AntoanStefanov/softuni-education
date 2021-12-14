from django.db import models
from django.utils import timezone
# Create your models here.
# Models for our movies app,
# these models are python classes that we use to represent our application data.
# So, here in our movies app, we're going to have models like genre and movie.

# INSTANTIATING AN OBJECT WITH THIS CLASS CREATES A ROW IN THE DATABASE WITH THE GIVEN FIELDS!
# SO THE OBJECT IS ACTUALLY THE ROW IN THE TABLER
class Genre(models.Model):
    # name is class attribute/variable/property
    # set name to an instance of a field class in django
    name = models.CharField(max_length=255)

    # we do that to represent the genre object in admin panel in the list with genres
    # THIS COULD BE USED TO SEE RECENT ACTIONS IN ADMIN PANEL AND MESSAGES FOR CREATED SUCCESSFUL,
    # bcs it overwrites the
    # GenreAdmin class in admin.py that list_display = ('id', 'name')
    def __str__(self):
        return self.name
    # we use the name of the genre to represent it as a string

# MOVIE HERE IS THE TABLE IN SQLITE
class Movie(models.Model):
    # all below is fields for a ROW(record)
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # on_delete ->
    # this tells django what should happen when a genre is deleted
    # let's assume that if the genre is deleted, all the movies associated with it should also be deleted
    # this is what we call cascading
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
#  next step is to tell django to synchronize our database with the models
#  we have defined in the movies app
