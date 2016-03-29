# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals

from django.views.generic import ListView

from ..models import DocumentGroup


class DocumentListView(ListView):
    model = DocumentGroup
    context_object_name = 'document_groups'
    template_name = 'documents/documents.html'
