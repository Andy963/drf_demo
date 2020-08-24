#!/usr/bin/env python
# encoding:utf-8
# Created by Andy @ 2020/8/24


from django.conf.urls import url

from api.views.user import UserView

urlpatterns = [
    url('user/$', UserView.as_view(), ),
    url('user/(?P<pk>\d+)/$', UserView.as_view(), name='user'),
]
