# -*- coding: utf-8 -*-
from django.conf.urls import url

from todos import views


urlpatterns = [
    url(r'^$', views.TodoList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.TodoDetail.as_view()),
]
