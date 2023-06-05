from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import MainAccountForm, SubAccountForm

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User Already Exists!")
                return redirect('register')
            else:
                # Create a new user
                user = User.objects.create_user(username=username, password=password)
                
                # Log in the user
                login(request, user)
                
                # Redirect to a success page
                messages.success(request, "User has been successfully registered!")
                return redirect('home')
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
    
    return render(request, 'myapp/register.html')




def add_main_account(request):
    if request.method == 'POST':
        form = MainAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Successfully Added!")
            return redirect('add_account')
    else:
        form = MainAccountForm()
        return render(request, 'myapp/add_account.html', {'form': form})
    
    return render(request, 'myapp/add_account.html', {'form': form})

def add_sub_account(request):
    form=SubAccountForm()
    if request.method == 'POST':
        form = SubAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Successfully Added!")
            return redirect('add_sub_account')
        else:
            form = SubAccountForm()
            return render(request, 'myapp/add_sub_account.html', {'form': form})
    
    return render(request, 'myapp/add_sub_account.html', {'form': form})