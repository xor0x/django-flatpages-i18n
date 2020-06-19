# Generated by Django 2.2.4 on 2020-06-19 11:44

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages_i18n', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage_i18n',
            name='content',
            field=martor.models.MartorField(blank=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='title'),
        ),
    ]
