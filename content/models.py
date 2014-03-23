from django.db import models
from django.contrib.auth.models import User
from goatnails.db.models import ImageWithThumbsField

# Create your models here.
class Editor(models.Model):
    user = models.ForeignKey(User)
    avatar = ImageWithThumbsField(upload_to="images", blank=True)
    real_pic = ImageWithThumbsField(upload_to="images", blank=True)
    bio = models.TextField()
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = ImageWithThumbsField(upload_to="images")
    credit = models.CharField(max_length=50)
    caption = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.caption

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Editor)
    credit = models.CharField(max_length=50)
    header_image = models.ForeignKey(Image)
    def __str__(self):
        return self.title

class Feature(models.Model):
    html = models.TextField()
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Editor)
    header_image = models.ForeignKey(Image)
    def __str__(self):
        return self.title

class Guide(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Editor)
    publish_date = models.DateTimeField()
    def __str__(self):
        return self.title
