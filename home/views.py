from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Contact


# from home.models import Contact


# Create your views here.


# home page
def index(request):
    # return HttpResponse("home page")
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, 'index.html')


# signup page
# noinspection PyBroadException
def signupUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()
        except:
            messages.error(request, 'Username already exists. Please select a different one.')
            return redirect('/signup')

        messages.success(request, 'Your account has been created successfully!')
        return redirect('/login')
    return render(request, 'signup.html')


# login page
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.error(request, 'Invalid username OR password!')
            return render(request, 'login.html')

    return render(request, 'login.html')


# logout page
def logoutUser(request):
    logout(request)
    return redirect('/login')


# about page
def about(request):
    return render(request, 'about.html')


# services page
def services(request):
    return render(request, 'services.html')


# contact page
def contact(request):
    if request.method == "POST":
        data = request.POST
        form = Contact(name=data.get('username'), email=data.get('email'),
                       phone=data.get('phone'), desc=data.get('desc'),
                       date=datetime.today())

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message is submitted successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'An error occurred while sending your Message!')
            return redirect('contact')

    return render(request, 'contact.html')


# products page
def products(request):
    return render(request, 'products.html')
