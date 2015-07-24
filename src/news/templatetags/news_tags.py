# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django import template

from ..models import News


register = template.Library()


@register.inclusion_tag('news/templatetags/latest_news.html')
def latest_news():
    news = News.objects.filter(is_published=True).order_by('-created')[:3]

    return {
        'news': news
    }
