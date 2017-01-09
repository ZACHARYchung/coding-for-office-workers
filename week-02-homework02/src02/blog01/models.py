from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length=30)
    view_count = models.IntegerField()
    contents = models.TextField()

class Comment(models.Model) :
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=300)
