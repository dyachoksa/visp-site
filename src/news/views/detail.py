# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.views.generic import DetailView

from ..models import News


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_published=True)
