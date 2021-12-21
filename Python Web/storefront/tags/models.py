from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag is applied to what object ?
    # if we delete a tag, we want to remove it from all the associated objects
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we need generic way to identify an object
    # To do that we need two pieces of information:

    # TYPE (product, video, article)
    # ID
    # Using these 2 pieces of information we can identify any object in our application
    # DATABASE TEMS - identify ANY RECORD IN ANY TABLES
    # ContentType is a model that represents the type of an object in our app
    
    # ContentType allows Generic relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
