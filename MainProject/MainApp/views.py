from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page_view(request):
    # return render(request, 'MainProject/MainApp/static/MainApp/home.html')
    return render(request, 'MainApp/index.html')
