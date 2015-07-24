# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from sitetree.utils import tree, item


sitetrees = (
    tree('main', items=[
        item('Home', 'home'),
        item('News', 'news:list', children=[
            item('{{ news.title }}', 'news:detail news.slug', in_menu=False)
        ]),
        item('Prices', 'prices:list'),
        item('About Us', '/pages/about/', url_as_pattern=False, children=[
            item('Internet', '/pages/about/', url_as_pattern=False),
            item('Cable TV', '/pages/about/tv/', url_as_pattern=False),
            item('Connect', '/pages/connect/', url_as_pattern=False),
        ]),
        item('Contacts', '/pages/contacts/', url_as_pattern=False),
    ]),

    tree('pages', items=[
        item('Internet', '/pages/about/', url_as_pattern=False),
        item('Cable TV', '/pages/about/tv/', url_as_pattern=False),
        item('Connect', '/pages/connect/', url_as_pattern=False),
    ]),

    tree('main_ru', items=[
        item('Главная', 'home'),
        item('Новости', 'news:list', children=[
            item('{{ news.title }}', 'news:detail news.slug', in_menu=False)
        ]),
        item('Цены', 'prices:list'),
        item('О Сети', '/pages/about/', url_as_pattern=False, children=[
            item('Интернет', '/pages/about/', url_as_pattern=False),
            item('Кабельное ТВ', '/pages/about/tv/', url_as_pattern=False),
            item('Подключение', '/pages/connect/', url_as_pattern=False),
        ]),
        item('Контакты', '/pages/contacts/', url_as_pattern=False),
    ]),

    tree('pages_ru', items=[
        item('Интернет', '/pages/about/', url_as_pattern=False),
        item('Кабельное ТВ', '/pages/about/tv/', url_as_pattern=False),
        item('Подключение', '/pages/connect/', url_as_pattern=False),
    ]),
)
