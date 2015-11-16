# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('request_date', models.DateTimeField(auto_now_add=True, verbose_name='request date')),
                ('customer_name', models.CharField(max_length=150, verbose_name='customer name')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('phone', models.CharField(max_length=25, verbose_name='phone number')),
                ('customer_comment', models.TextField(default=None, null=True, verbose_name='comment', blank=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'request',
                'verbose_name_plural': 'requests',
            },
        ),
    ]
