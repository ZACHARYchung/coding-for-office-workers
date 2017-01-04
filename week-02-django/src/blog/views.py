# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
# Create your views here.
from .models import Article

def index(request):
    # random_number= randint(1,10)
    # return HttpResponse("Hello, world. {}".format(random_number))
    # return HttpResponse("Hello, world. You're at the index.")
    # name = "marco"
    # return render(request,"index.html",{"name":name})
    article_list = Article.objects.all() #Load everything from Article
    # Article.objects.create(
    #     title="hello",
    #     contents="thisistest",
    #     view_count=0
    # )
    ctx={
        "article_list" : article_list
    } #created a dictionary called ctx(context)
    return render(request,"index.html",ctx)
