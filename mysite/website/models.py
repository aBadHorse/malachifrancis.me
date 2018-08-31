from django.db import models
from django.contrib.auth.models import AbstractUser

#TODO add user specific flags and fields to User
class User(AbstractUser):
    perm = models.IntegerField(default=1, verbose_name='permission level')

    def __str__(self):
        return self.email


class NavOption(models.Model):
    name = models.CharField(max_length=15, verbose_name='display name')
    path = models.CharField(max_length=127, verbose_name='URL pattern')
    position = models.IntegerField()
    perm_req = models.IntegerField(verbose_name='permission level required')

    def __str__(self):
        return self.name


class MenuOption(models.Model):
    category = models.ForeignKey('NavOption', on_delete=models.PROTECT)
    name = models.CharField(max_length=15, verbose_name='display name')
    path = models.CharField(max_length=127, verbose_name='URL pattern')
    position = models.IntegerField()
    perm_req = models.IntegerField(verbose_name='permission level required')

    def __str__(self):
        return self.name


class Content(models.Model):
    category = models.ForeignKey('NavOption', on_delete=models.PROTECT)
    title = models.CharField(max_length=31)
    brief = models.TextField(verbose_name='preface text',blank=True, null=True)
    text = models.TextField(verbose_name='body text', blank=True, null=True)
    footer = models.TextField(verbose_name='footer text', blank=True, null=True)
    date = models.DateField(verbose_name='publish date')
    image = models.CharField(max_length=31, verbose_name='image name', blank=True, null=True)
    embed = models.CharField(max_length=127, verbose_name='embed url', blank=True, null=True)

    def __str__(self):
        return self.title
