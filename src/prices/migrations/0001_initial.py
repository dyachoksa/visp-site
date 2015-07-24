# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50, verbose_name='title')),
                ('price', models.DecimalField(verbose_name='price', max_digits=10, decimal_places=2)),
                ('speed', models.CharField(max_length=15, verbose_name='speed')),
                ('description', models.TextField(max_length=200, null=True, verbose_name='description', blank=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
            },
        ),
        migrations.AlterIndexTogether(
            name='price',
            index_together=set([('created', 'is_published')]),
        ),
    ]
