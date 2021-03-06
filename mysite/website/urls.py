from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view()),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('about/resume', ResumeView.as_view(), name='resume'),
    path('art/', ArtView.as_view(), name='art'),
    path('dev/', DevView.as_view(), name='dev'),
    path('dev/deckalyzer', DeckalyzerView.as_view(), name='deckalyzer'),
    path('music/', MusicView.as_view(), name='music'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView, {'next_page': '/'}, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('account/', UpdateUserView.as_view(), name='account'),
]
