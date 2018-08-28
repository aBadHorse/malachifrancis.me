from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Content, NavOption, MenuOption, User
from .forms import LoginForm, RegisterUserForm

class BaseView(View):
    nav_options = NavOption.objects.order_by('position')
    template_name = 'website/content-list.html'

    def get(self, request):
        context = {
            'content_list': self.content_list,
            'menu_options': self.menu_options,
            'page_style': self.page_style,
            'page_title': self.page_title,
            'nav_options': self.nav_options,
        }
        return render(request, self.template_name, context)


class AboutView(BaseView):
    content_list = Content.objects.filter(category__name='about me').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='about me').order_by('position')
    page_style = 'about.min.css'
    page_title = 'about me'


class ArtView(BaseView):
    content_list = Content.objects.filter(category__name='art').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='art').order_by('position')
    page_style = 'art.min.css'
    page_title = 'art'


class DevView(BaseView):
    content_list = Content.objects.filter(category__name='dev').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='dev').order_by('position')
    page_style = 'dev.min.css'
    page_title = 'dev'


class HomeView(BaseView):
    content_list = Content.objects.all().order_by('-date')[:5]
    menu_options = None
    page_style = 'home.min.css'
    page_title = 'home'


class MusicView(BaseView):
    content_list = Content.objects.filter(category__name='music').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='music').order_by('position')
    page_style = 'music.min.css'
    page_title = 'music'


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    success_url = 'website:home'
    template_name = 'website/register.html'
