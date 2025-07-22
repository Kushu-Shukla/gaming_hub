from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    return render(request, 'core/home.html')

def games_view(request):
    return render(request, 'core/games.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    return render(request, 'core/register.html')


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"Contact from {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            return redirect('home')  
    return render(request, 'core/contact.html', {'form': form})

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # change to your home url name
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'core/login.html')
