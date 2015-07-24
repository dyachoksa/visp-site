# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created'], 'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='is published'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created', db_index=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='%Y', null=True, verbose_name='image', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]
