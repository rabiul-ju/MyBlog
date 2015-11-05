# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myblog',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created='true')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=4000)),
                ('tag', models.CharField(max_length=50)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
