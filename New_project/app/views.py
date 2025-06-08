from django.shortcuts import render, redirect
from .models import ContactEnquiry  # Import the ContactEnquiry model
from .models import Signup  # Import the Login model
from django.http import HttpResponse

def index(request):
    return render (request, 'index.html')  # Render the index.html template

def project(request):
    return render (request, 'project.html')  # Render the about.html template

def contact(request):
    return render (request, 'contact.html')  # Render the contact.html template

def skills(request):
    return render (request, 'skills.html')  # Render the blog.html template

def signup(request):
    return render (request, 'signup.html')  # Render the blog.html template

def login(request):
    return render (request, 'login.html')  # Render the blog.html template
# Create your views here.

def saveenquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en=ContactEnquiry(name=name, email=email, phone=phone, message=message)
        en.save()
        return redirect('contact')  # Redirect to the contact page after saving the enquiry
    else:
        return HttpResponse("Invalid request method.") 
    
def savesignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        sl=Signup(username=username, password=password, email=email)
        sl.save()
        return redirect('index')  # Redirect to the home page after login
    else:
        return HttpResponse("Invalid request method.")