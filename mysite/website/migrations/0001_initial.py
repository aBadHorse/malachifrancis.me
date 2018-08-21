# Generated by Django 2.0.5 on 2018-05-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('path', models.CharField(max_length=127)),
                ('position', models.IntegerField()),
                ('perm_req', models.IntegerField(verbose_name='permission level required')),
            ],
        ),
    ]
