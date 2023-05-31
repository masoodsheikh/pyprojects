from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'myapp/index.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "Something went wrong, try again!")
            return redirect('login')
    else:
        return render(request, "myapp/login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You are successfully logged out!")
    return redirect('home')

def register(request):
    pass