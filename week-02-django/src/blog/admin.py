from django.contrib import admin

# Register your models here.
from .models import Article , Comment

@admin.register(Article, Comment)
class BlogAdmin(admin.ModelAdmin):
    pass
