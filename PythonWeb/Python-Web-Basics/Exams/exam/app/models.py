import re

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

VALIDATE_USERNAME_EXCEPTION_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validate_only_letters_numbers_underscore(value):
    if not re.match("^[A-Za-z0-9_]*$", value):
        raise ValidationError(VALIDATE_USERNAME_EXCEPTION_MESSAGE)


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_only_letters_numbers_underscore,
        ]
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ]
    )


class Item(models.Model):
    class Meta:
        # ORDER BY THE FIELDS THAT ARE GIVEN
        ordering = ('album_name', 'price',)

    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    PRICE_MIN_VALUE = 0.0

    GENRE_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]

    # IS UNIQUE ENOUGH ?
    album_name = models.CharField(max_length=ALBUM_NAME_MAX_LENGTH, unique=True)

    artist = models.CharField(max_length=ARTIST_MAX_LENGTH)

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(blank=True, null=True)

    image = models.URLField()

    description = models.TextField(null=True, blank=True)

    price = models.FloatField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE)
        ]
    )
