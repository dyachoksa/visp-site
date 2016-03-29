# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class DocumentGroup(TimeStampedModel):
    title = models.CharField(_('title'), max_length=255)
    position = models.SmallIntegerField(_('position'), default=1, db_index=True)

    class Meta:
        ordering = ['position']
        verbose_name = _('document group')
        verbose_name_plural = _('document groups')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Document(TimeStampedModel):
    document_group = models.ForeignKey(DocumentGroup, verbose_name=_('document group'), db_index=True)
    title = models.CharField(_('title'), max_length=255)
    position = models.IntegerField(_('position'), default=1, db_index=True)
    file = models.FileField(_('file'), max_length=255, upload_to='documents/%Y')

    class Meta:
        index_together = (
            ('document_group', 'position'),
        )
        ordering = ['document_group', 'position']
        verbose_name = _('document')
        verbose_name_plural = _('documents')

    def __str__(self):
        return self.title
