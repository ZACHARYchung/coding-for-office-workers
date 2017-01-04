from django.db import models

# Create your models here.
#아티클 이라는 클래스를 만드는데 import 한 models 에서 model이라는 클래스를 가져온것.
class Article(models.Model):
    title = models.CharField(max_length=30) #charfield 는 항상 맥스 길이가 있어야 한다.
    contents = models.TextField()
    view_count= models.IntegerField()

    def __str__(self): #클래스 안에 함수 만들때 이름에 언더바 두개 넣는 경우 많다. 그리고 꼭 self해줘야함
        return "{} ({})".format(self.title, self.view_count)


class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=100)
