# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import News


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title'],
    }

    date_hierarchy = 'created'

    search_fields = ['title', 'content']

    list_display = ['title', 'is_published', 'has_image', 'created', 'updated']
    list_display_links = ['title']
    list_filter = ['is_published', 'created']

    def has_image(self, obj):
        """
        :type obj: News
        """
        return True if obj.image else False
    has_image.boolean = True
    has_image.short_description = _('has image')


admin.site.register(News, NewsAdmin)
