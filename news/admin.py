from django.contrib import admin
from .models import Category, Author, Post, Comment


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
