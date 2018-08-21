from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),
    path('art/', views.home, name='art'),
    path('dev/', views.dev, name='dev'),
]
