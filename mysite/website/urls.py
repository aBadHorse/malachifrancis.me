from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from website.views import *

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view()),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('art/', ArtView.as_view(), name='art'),
    path('dev/', DevView.as_view(), name='dev'),
    path('music/', MusicView.as_view(), name='music'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('register/', RegisterUserView.as_view())
]
