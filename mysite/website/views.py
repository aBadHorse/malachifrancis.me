from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Content, NavOption
# Create your views here.
def home(request):
    nav_options = NavOption.objects.order_by('position')
    context = {
        'page_title': "home",
        'nav_options': nav_options,
    }
    return render(request, 'website/home.html', context)


def about(request):
    nav_options = NavOption.objects.order_by('position')
    content_list = Content.objects.filter(category__name='about me').order_by('-date')

    context = {
        'page_title': "about me",
        'nav_options': nav_options,
        'content_list': content_list,
    }
    return render(request, 'website/about.html', context)


def dev(request):
    nav_options = NavOption.objects.order_by('position')
    content_list = Content.objects.filter(category__name='dev').order_by('-date')

    context = {
        'page_title': "dev",
        'nav_options': nav_options,
        'content_list': content_list,
    }
    return render(request, 'website/dev.html', context)


def music(request):
    nav_options = NavOption.objects.order_by('position')
    content_list = Content.objects.filter(category__name='music').order_by('-date')

    context = {
        'page_title': "music",
        'nav_options': nav_options,
        'content_list': content_list,
    }
    return render(request, 'website/about.html', context)