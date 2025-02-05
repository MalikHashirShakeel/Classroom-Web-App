from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Error Handling
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif len(password1) < 6:
            messages.error(request, "Password must be at least 6 characters.")
        else:
            user = User.objects.create(username=username, email=email, password=make_password(password1))
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('classroom_list')  # Redirect to classroom list after registration

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('classroom_list')  # Redirect to classroom list after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')
