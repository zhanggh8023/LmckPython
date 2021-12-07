# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 20:47
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day04_class_view.py
# @Software: PyCharm
import time

from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__)


def log_time(f):
    def decorator(*args, **kwargs):
        print(f'{time.time()}')
        return f(*args, **kwargs)
        # 装饰器返回必须是视图函数的返回值

    return decorator


class ProjectView(View):
    methods = ['GET', 'POST']
    decorators = (log_time,)

    # 分配请求
    def get_project(self):
        return 'get'

    def post(self):
        return 'post'

    # def get_all_project(self):
    #     return 'projects'

    def dispatch_request(self):
        dispatch_pattern = {"GET": self.get_project, "POST": self.post}
        method = request.method
        dispatch_pattern.get(method)
        return dispatch_pattern.get(method)()
        # return 'project'


f = ProjectView.as_view('project')
# log_time(f)
# 装饰器使用要：1、@log_time;2:log_time(f)

app.add_url_rule('/project', view_func=ProjectView.as_view('project'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)
