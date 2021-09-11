from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'site_display/index.html')


def account(request):
    return render(request, 'site_display/account.html')


def authorization(request):
    return render(request, 'site_display/authorization.html')


def performers(request):
    return render(request, 'site_display/performers.html')


def registration(request):
    return render(request, 'site_display/registration.html')


def genres(request):
    return render(request, 'site_display/genres.html')