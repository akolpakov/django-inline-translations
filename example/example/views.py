from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def login_view(request):
    try:
        User.objects.get(username='example')
    except User.DoesNotExist:
        User.objects.create_superuser(username='example', email='example@example.com', password='example')

    user = authenticate(username='example', password='example')
    login(request, user)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')
