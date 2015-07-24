# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.conf.urls import url

from .views.detail import NewsDetailView
from .views.list import NewsListView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w\d\-_]+)/$', NewsDetailView.as_view(), name='detail'),
]
