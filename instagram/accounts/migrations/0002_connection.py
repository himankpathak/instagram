# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
