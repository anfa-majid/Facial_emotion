from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages, auth
from .forms import SignupForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'registrationapp/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully signed up. Please login.")
            return redirect('registrationapp:login')  # Ensure named URL pattern is configured in urls.py
    else:
        form = SignupForm()
    return render(request, 'registrationapp/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')  # Ensure named URL pattern 'home' is configured
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'registrationapp/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('registrationapp:login')  # Use the 'registrationapp:login' named URL
