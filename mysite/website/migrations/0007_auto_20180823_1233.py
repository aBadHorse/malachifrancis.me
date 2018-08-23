# Generated by Django 2.0.5 on 2018-08-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20180823_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='brief',
            field=models.TextField(blank=True, null=True, verbose_name='preface text'),
        ),
        migrations.AddField(
            model_name='content',
            name='footer',
            field=models.TextField(blank=True, null=True, verbose_name='footer text'),
        ),
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='body text'),
        ),
    ]