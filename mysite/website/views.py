from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from deckalyzer import deckalyzer
from .models import Content, NavOption, MenuOption, User
from .forms import LoginForm, RegisterUserForm, UpdateUserForm, DeckalyzerForm


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
    content_list = Content.objects.filter(category__name='about').order_by('-date')
    menu_options = MenuOption.objects.filter(category__name='about').order_by('position')
    page_style = 'about.min.css'
    page_title = 'about'


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


class DeckalyzerView(DevView):
    template_name = 'website/deckalyzer.html'

    def get(self, request):
        form = DeckalyzerForm()
        context = {
            'content_list': self.content_list,
            'menu_options': self.menu_options,
            'page_style': self.page_style,
            'page_title': self.page_title,
            'nav_options': self.nav_options,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = DeckalyzerForm(request.POST)
        if form.is_valid():
            deck_name = form.cleaned_data.get('deck_name')
            deck_descr = form.cleaned_data.get('description')
            deck_data = form.cleaned_data.get('card_list')
            deck_record = deckalyzer.run(request.user.username, deck_name, deck_descr, deck_data)
            context = {
                'content_list': self.content_list,
                'menu_options': self.menu_options,
                'page_style': self.page_style,
                'page_title': self.page_title,
                'nav_options': self.nav_options,
                'deck': deck_record
            }
            return render(request, self.template_name, context)


class ResumeView(AboutView):
    template_name = 'website/resume.html'
    page_style = 'pdf.min.css'


class LoginUserView(View):
    template_name = 'website/form.html'

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data.get('user_password')
            user_name = form.cleaned_data.get('user_name')
            user = authenticate(username=user_name, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
        context = {
            'form': form,
            'page_style': 'forms.min.css',
            'nav_options': NavOption.objects.order_by('position'),
            'page_title': 'login',
            'form_title': 'Login',
            'error_msg': 'User name and/or password are invalid',
        }
        return render(request, self.template_name, context)

    def get(self, request):
        context = {
            'form': LoginForm(),
            'page_style': 'forms.min.css',
            'nav_options': NavOption.objects.order_by('position'),
            'page_title': 'login',
            'form_title': 'Login'
        }
        return render(request, self.template_name, context)


class RegisterUserView(CreateView):
    template_name = 'website/form.html'

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password1')
            user_name = form.cleaned_data.get('username')
            user = authenticate(username=user_name, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
        context = {
            'form': form,
            'page_style': 'forms.min.css',
            'nav_options': NavOption.objects.order_by('position'),
            'page_title': 'register',
            'form_title': 'Register new account'
        }
        return render(request, self.template_name, context)

    def get(self, request):
        context = {
            'form': RegisterUserForm(),
            'page_style': 'forms.min.css',
            'nav_options': NavOption.objects.order_by('position'),
            'page_title': 'register',
            'form_title': 'Register new account'
        }
        return render(request, self.template_name, context)


class UpdateUserView(View):
    template_name = 'website/form.html'

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {
            'form': form,
            'page_style': 'forms.min.css',
            'nav_options': NavOption.objects.order_by('position'),
            'page_title': 'register',
            'form_title': 'Update account info'
        }
        return render(request, self.template_name, context)

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        context = {
            'form': UpdateUserForm(instance=user),
            'page_style': 'forms.min.css',
            'nav_options': NavOption.objects.order_by('position'),
            'page_title': 'register',
            'form_title': 'Update account info'
        }
        return render(request, self.template_name, context)
