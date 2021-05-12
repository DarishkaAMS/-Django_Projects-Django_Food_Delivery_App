from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page_view(request):
    template = 'MainApp/index.html'
    return render(request, template)
