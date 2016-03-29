# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('position', models.IntegerField(default=1, verbose_name='position', db_index=True)),
                ('file', models.FileField(upload_to='documents/%Y', max_length=255, verbose_name='file')),
            ],
            options={
                'ordering': ['document_group', 'position'],
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('position', models.SmallIntegerField(default=1, verbose_name='position', db_index=True)),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'document group',
                'verbose_name_plural': 'document groups',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='document_group',
            field=models.ForeignKey(verbose_name='document group', to='documents.DocumentGroup'),
        ),
        migrations.AlterIndexTogether(
            name='document',
            index_together=set([('document_group', 'position')]),
        ),
    ]
