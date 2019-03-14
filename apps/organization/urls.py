# !/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'SIRIUS'
__date__ = '2018/10/1-001 17:29'
from django.urls import path, include

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

app_name = '[org]'
urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    path('home/<org_id>', OrgHomeView.as_view(), name='org_home'),
    path('course/<org_id>', OrgCourseView.as_view(), name='org_course'),
    path('desc/<org_id>', OrgDescView.as_view(), name='org_desc'),
    path('teacher/<org_id>', OrgTeacherView.as_view(), name='org_teacher'),
    path('add_fav/', AddFavView.as_view(), name='add_fav'),
]
