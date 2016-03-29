# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import DocumentGroup, Document


class DocumentGroupsAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'modified']
    list_display = ['title', 'position', 'created']


class DocumentsAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'modified']
    list_display = ['title', 'document_group', 'position', 'created']


admin.site.register(DocumentGroup, DocumentGroupsAdmin)
admin.site.register(Document, DocumentsAdmin)
