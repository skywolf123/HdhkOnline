# !/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'SIRIUS'
__date__ = '2018/9/25-025 11:28'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSettings(object):
    enable_themes = True    # 启用主题功能
    use_bootswatch = True   # 启用多主题选择


class CommSettings(object):
    site_title = '菡萏花开-后台管理系统'
    site_footer = '菡萏花开'
    menu_style = 'accordion'    # 可折叠


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, CommSettings)
