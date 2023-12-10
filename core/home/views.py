from django.shortcuts import render

def home(request):
    template = 'index.html'
    context = {
        'title': 'Home',
    } 
    return render(request, template, context) 
