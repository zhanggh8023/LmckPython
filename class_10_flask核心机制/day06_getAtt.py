# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 21:40
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day06_getAtt.py
# @Software: PyCharm
"""
# REST
设计测试项目里面的API

url                    方法            说明
/projects/             GET            x项目列表
/projects/             POST         c创建一个项目
/projects/<id>         GET          显示一个项目
/projects/<id>         PUT          更新一个项目
/projects/<id>         GET          删除一个项目

"""
from flask import Flask, request

from flask.views import MethodView

app = Flask(__name__)


class UserView(MethodView):
    def get(self, project_id):
        if project_id is None:
            return 'GET all project'
        print('get')
        return f'get  {project_id}'

    def post(self):
        print('post')
        return f'post'

    def put(self, project_id):
        print('put')
        return f'put  {project_id}'

    def delete(self, project_id):
        print('delete')
        return f'delete  {project_id}'


f = UserView.as_view('project')
app.add_url_rule('/projects/<project_id>', view_func=f, methonds=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/projects/', defaults={"project_id": None}, view_func=f, methonds=['GET', ])

if __name__ == '__main__':
    app.run(debug=True)

"""class MethodView:
    # 分配请求
    def get(self):
        print('get')
        return 'get'

    def post(self):
        print('post')
        return 'post'

    def dispatch_request(self):
        func = getattr(self, 'get', None)
        print(func)
        return func() # get()


MethodView().dispatch_request()"""
