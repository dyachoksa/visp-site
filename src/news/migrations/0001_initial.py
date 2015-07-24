# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name='image', blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
        ),
    ]
