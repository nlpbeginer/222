from django.http import HttpResponse
from django.shortcuts import render


def admin(request):
    return render(request, 'admin.html')


def index(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'sign-up.html')


def user(request):
    return render(request, 'dashboard.html')


def paper_submit(request):
    return render(request, 'paper-submit.html')


def invitation(request):
    return render(request, 'invitation.html')
