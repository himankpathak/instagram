# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('slug', models.SlugField(max_length=10, unique=True, default=posts.models.generate_id)),
                ('photo', models.FileField(upload_to='posts_photo')),
                ('caption', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='post')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
