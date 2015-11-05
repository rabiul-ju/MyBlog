# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20151022_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(null=True, max_length=255, default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='myblog',
            name='tag',
        ),
        migrations.AddField(
            model_name='myblog',
            name='author',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='title',
            field=models.CharField(max_length=100, default='habijabi'),
        ),
        migrations.AddField(
            model_name='myblog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
