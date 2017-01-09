from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.




def index(request):
    # return HttpResponse("Hello, world. You're at the blog01 index.")
    name = "marco"
    return render(request, "index.html",{ name : "name"})
