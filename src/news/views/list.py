# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.views.generic import ListView

from ..models import News


class NewsListView(ListView):
    model = News

    def get_queryset(self):
        return News.objects.filter(is_published=True)
