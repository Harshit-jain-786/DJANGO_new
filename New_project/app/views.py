from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'index.html')  # Render the index.html template

def about(request):
    return render (request, 'about.html')  # Render the about.html template

def contact(request):
    return render (request, 'contact.html')  # Render the contact.html template

def blog(request):
    return render (request, 'blog.html')  # Render the blog.html template
# Create your views here.
