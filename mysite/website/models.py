from django.db import models

# Create your models here.
class NavOption(models.Model):
    name = models.CharField(max_length=15, verbose_name='display name')
    icon = models.CharField(max_length=31, verbose_name='fa class name', blank=True, null=True)
    path = models.CharField(max_length=127, verbose_name='URL pattern')
    position = models.IntegerField()
    perm_req = models.IntegerField(verbose_name='permission level required')

    def __str__(self):
        return self.name


class Content(models.Model):
    category = models.ForeignKey('NavOption', on_delete=models.PROTECT)
    title = models.CharField(max_length=31)
    text = models.TextField()
    date = models.DateField(verbose_name='publish date')
    image = models.CharField(max_length=31, verbose_name='image name', blank=True, null=True)

    def __str__(self):
        return self.title
