#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-14 20:17:29
# @Author  : Job (Job@6box.net)
# @Link    : http://www.6box.net
# @Version : $Id$

from django.conf.urls import url
from update import views

urlpatterns = [
    url(r'^$', views.updates, name='update'),
    url(r'^version_get/$', views.version_get, name='version_get'),
    url(r'^version_update/$', views.version_update, name='version_update'),
    url(r'^info/$', views.info, name='info'),



]
