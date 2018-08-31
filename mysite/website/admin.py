from django.contrib import admin

from .models import Content, NavOption, MenuOption, User

# Register your models here.
admin.site.register(Content)
admin.site.register(MenuOption)
admin.site.register(NavOption)
admin.site.register(User)
