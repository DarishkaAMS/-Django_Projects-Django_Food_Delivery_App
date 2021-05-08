from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page_view(request):
    template = 'MainApp/index.html'
    return render(request, template)


def login_page_view(request):
    # return render(request, 'MainProject/MainApp/static/MainApp/home.html')
    return render(request, 'MainApp/login.html')


def register_page_view(request):
    # return render(request, 'MainProject/MainApp/static/MainApp/home.html')
    return render(request, 'MainApp/register.html')
