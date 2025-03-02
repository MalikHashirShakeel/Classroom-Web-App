from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message

def about(request):
    """View to display the About page and handle message submissions."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Message.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent!')
        return redirect('about')

    return render(request, 'about/about.html')