# Generated by Django 2.0.5 on 2018-05-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navoption',
            name='name',
            field=models.CharField(max_length=15, verbose_name='display name'),
        ),
        migrations.AlterField(
            model_name='navoption',
            name='path',
            field=models.CharField(max_length=127, verbose_name='URL pattern'),
        ),
    ]
