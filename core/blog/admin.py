from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author')
    list_filter = ('category', 'date_published', 'author')
    search_fields = ('title', 'content', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user' )
    list_filter = ('post', 'user')
    search_fields = ('post__title', 'content', 'user__username')
