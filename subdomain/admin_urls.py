__author__ = 'utkbansal'
# This is a temporary hack to get the emulate admin.py module for the
# django admin site

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include(admin.site.urls)),
]
