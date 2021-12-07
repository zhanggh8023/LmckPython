# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 21:24
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day05_method_view.py
# @Software: PyCharm

"""
MethodView
"""
import time

from flask import Flask, request, render_template
from flask.views import View, MethodView

app = Flask(__name__)


def log_time(f):
    def decorator(*args, **kwargs):
        print(f'{time.time()}')
        return f(*args, **kwargs)
        # 装饰器返回必须是视图函数的返回值

    return decorator


class ProjectView(MethodView):
    # 分配请求
    def get(self):
        print('get')
        return 'get'

    def post(self):
        print('post')
        return 'post'


f = ProjectView.as_view('project')
app.add_url_rule('/project', view_func=f)
if __name__ == '__main__':
    app.run(debug=True)
