from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import re

def is_strong_password(password):
    """Check if the password meets security requirements."""
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in "!@#$%^&*()-_=+" for c in password)
    )

def register(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Username Validation
        if not re.match(r'^[a-zA-Z0-9_]{4,}$', username):
            messages.error(request, "Username must be at least 4 characters and contain only letters, numbers, and underscores.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")

        # Email Validation
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messages.error(request, "Enter a valid email address.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")

        # Password Validation
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif not is_strong_password(password1):
            messages.error(request, "Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, a number, and a special character (!@#$%^&*()-_=+).")

        else:
            user = User.objects.create(username=username, email=email, password=make_password(password1))
            login(request, user)
            messages.success(request, "Registration successful! Keep your credentials safe.")
            return redirect('classroom_list')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('classroom_list')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')
