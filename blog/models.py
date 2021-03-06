from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image')
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
