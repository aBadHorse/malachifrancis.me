from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from website.views import *

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view()),
    path('art/', ArtView.as_view()),
    path('dev/', DevView.as_view()),
    path('music/', MusicView.as_view()),
    path('login/', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('register/', RegisterUserView.as_view())
]
