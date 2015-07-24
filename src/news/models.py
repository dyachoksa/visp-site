# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


@python_2_unicode_compatible
class News(models.Model):
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    is_published = models.BooleanField(verbose_name=_('is published'), default=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='%Y', blank=True, null=True)
    content = RichTextField(verbose_name=_('content'))
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True, db_index=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = pgettext_lazy('singular', 'news')
        verbose_name_plural = _('news')

    def __str__(self):
        return self.title
