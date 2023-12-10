from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Comment
from django.contrib.auth.models import User

def user_list(request):
    users = User.objects.all()
    template = 'blog/user_list.html'
    context = {
        'users': users,
        'title': 'Users List',
        }
    
    return render(request, template, context)

def category_list(request):
    categories = Category.objects.all()
    template = 'blog/categories.html'
    context = {
        'categories': categories,
        'title': 'Category List'
            }
    return render(request, template, context)

def post_list(request):
    posts = Post.objects.all()
    template = 'blog/blogs.html'
    context = {
        'posts': posts,
        'title': 'Post List'
            }
    return render(request, template, context)

def comment_list(request):
    comments = Comment.objects.all()
    template = 'blog/comments.html'
    context = {
        'comments': comments,
        'title': 'Comment List'
               }
    return render(request, template, context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    template = 'blog/blogdetails.html'
    context = {
        'post': post, 
        'comments': comments,
        'title': post.title}
    return render(request, template, context)
