from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import re
from captcha.fields import CaptchaField
from django import forms

class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()

#------------------------------------------------------------

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
        captcha_form = CaptchaTestForm(request.POST)

        # CAPTCHA Validation
        if not captcha_form.is_valid():
            messages.error(request, "Invalid CAPTCHA. Please try again.")
        # Username Validation
        elif not re.match(r'^[a-zA-Z0-9_]{4,}$', username):
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

    else:
        captcha_form = CaptchaTestForm()

    return render(request, 'register.html', {'captcha_form': captcha_form})

#------------------------------------------------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password']
        captcha_form = CaptchaTestForm(request.POST)

        # CAPTCHA Validation
        if not captcha_form.is_valid():
            messages.error(request, "Invalid CAPTCHA. Please try again.")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")

                # Check if user is a superuser
                if user.is_superuser:
                    return redirect('/admin/')  # Redirect to Django admin panel

                return redirect('classroom_list') 
            else:
                messages.error(request, "Invalid username or password.")

    else:
        captcha_form = CaptchaTestForm()

    return render(request, 'login.html', {'captcha_form': captcha_form})

#------------------------------------------------------------

def user_logout(request):
    """Log out the user and redirect to the homepage."""
    logout(request)
    return redirect('/')  

#------------------------------------------------------------