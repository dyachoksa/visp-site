"""visp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from customers.views.leave_request import LeaveRequestView
from news import urls as news_urls
from pages.views.home import HomePageView
from prices import urls as prices_urls

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^leave-request/$', LeaveRequestView.as_view(), name='leave_request'),
    url(r'^news/', include(news_urls, namespace='news')),
    url(r'^prices/', include(prices_urls, namespace='prices')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
