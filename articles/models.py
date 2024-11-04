from django.db import models

# Create your models here.

from django.db import models


# Simple Article Model
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


# Simple Like model
class Like(models.Model):
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, related_name="like"
    )
    count = models.IntegerField(default=0)

    # user - this would have been here if auth was implemented
