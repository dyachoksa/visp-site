# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.flatpages.forms import FlatpageForm as BaseFlatPageForm


class FlatPageForm(BaseFlatPageForm):
    class Meta:
        widgets = {
            'content': CKEditorUploadingWidget()
        }
