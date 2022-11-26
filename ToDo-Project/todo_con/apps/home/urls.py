# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.conf.urls import url
from .views import detail_view


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('new-task.html', views.add_task, name="add"),
    path('task-list.html', views.list_view, name="list"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^detail/(?P<id>\d+)$', views.detail_view, name='detail'),
    path('search/', views.searchBar, name='search'),
   

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
