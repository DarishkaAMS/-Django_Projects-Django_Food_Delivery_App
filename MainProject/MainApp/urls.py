from django.urls import path
from .views import home_page_view, login_page_view, register_page_view

urlpatterns = [
    path('', home_page_view, name='index'),

    path('login', login_page_view, name='login'),
    path('register', register_page_view, name='register'),

    path('', home_page_view, name='about'),
    path('', home_page_view, name='about'),
    path('', home_page_view, name='services'),
    path('', home_page_view, name='portfolio-1'),
    path('', home_page_view, name='single-project'),
    path('', home_page_view, name='single-project-2'),
    path('', home_page_view, name='single-post'),
    path('', home_page_view, name='contact'),
]
