from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import View

from .models import Content, NavOption, MenuOption
from .forms import LoginForm

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
    page_style = 'about.css'
    page_title = 'about me'


class ArtView(BaseView):
    content_list = Content.objects.filter(category__name='art').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='art').order_by('position')
    page_style = 'art.css'
    page_title = 'art'


class DevView(BaseView):
    content_list = Content.objects.filter(category__name='dev').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='dev').order_by('position')
    page_style = 'dev.css'
    page_title = 'dev'


class HomeView(BaseView):
    content_list = Content.objects.all().order_by('-date')[:5]
    menu_options = None
    page_style = 'home.css'
    page_title = 'home'


class MusicView(BaseView):
    content_list = Content.objects.filter(category__name='music').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='music').order_by('position')
    page_style = 'music.css'
    page_title = 'music'
