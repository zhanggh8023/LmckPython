# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 15:50
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: urls.py
# @Software: PyCharm

import views
from day02_views_视图函数的分离 import app

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/cases', view_func=views.cases)
