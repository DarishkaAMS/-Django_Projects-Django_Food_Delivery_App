from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login_page_view(request):
    # return render(request, 'MainProject/MainApp/static/MainApp/home.html')
    return render(request, 'account/login.html')


def register_page_view(request):
    # return render(request, 'MainProject/MainApp/static/MainApp/home.html')
    return render(request, 'account/register.html')
