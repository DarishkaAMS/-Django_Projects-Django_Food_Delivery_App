from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm
# Create your views here.


def login_page_view(request):
    # return render(request, 'MainProject/MainApp/static/MainApp/home.html')
    return render(request, 'account/login.html')


# def register_page_view(request):
#     # return render(request, 'MainProject/MainApp/static/MainApp/home.html')
#     return render(request, 'account/register.html')


def register_page_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.username}")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("index")
        else:
            context['registration_form'] = form

    return render(request, 'account/register.html', context)
