# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 19:52
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day03_views_项目.py
# @Software: PyCharm

"""
1、通过<id>或者？去构建路由
2、获取所有的测试用例，获取单个测试用例
写一个视图函数、
3、get/post/delete,请求，不同的视图
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'GET 所有的项目'
    elif request.method == 'POST':
        return '创建一个'


@app.route('/list_projects', methods=['GET', 'POST'])
def list_projects():
    if request.method == 'GET':
        return 'GET 所有的项目'
    elif request.method == 'POST':
        return '创建一个'


@app.route('/list_project', methods=['GET', 'DELETE'])
def list_projects():
    if request.method == 'GET':
        return 'GET 所有的项目'
    elif request.method == 'DELETE':
        return '删除一个项目'


# @app.route('/create_projects',methods=['POST'])
# def create_projects():
#     return 'post 获取所有'
#
# @app.route('/get_projects/<id>',methods=['GET'])
# def get_projects(id):
#     return f'获取单个{id}'

@app.route('project/<p_id>', methods=['GET'])
def projects(p_id):
    return f'单个{p_id}'


if __name__ == '__main__':
    app.run(debug=True)
