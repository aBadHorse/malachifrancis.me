from django.urls import path

from . import views
from website.views import *

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view()),
    path('art/', ArtView.as_view()),
    path('dev/', DevView.as_view()),
    path('music/', MusicView.as_view()),
]
