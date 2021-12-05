# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 23:11
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 01_route_路由.py
# @Software: PyCharm

from flask import Flask, request
from flask.views import View, MethodView
import uuid

print(uuid.uuid4())

app = Flask(__name__)


# @app.route('/cases/<int:id>') # int/float/string/path/uuid(唯一id)
# @app.route('/cases')
# def get_case(id):
#     # id = request.args.get('id')
#     return f'{id}'

@app.route('/')
def home():
    return 'home'


@app.route('/cases', redirect_to='/')
# redirect_to重定向：不会去执行视图函数，也就是下面的函数会跳过，直接运行home
def get_case():
    return 'case'


print(app.url_map)


# 路由：URL,视图函数的绑定关系，端点

# 默认；defaults=｛‘id’:3｝
# 视图函数定义 id=3
@app.route('/cases/', methods=['POST'], endpoint='case', redirect_to='/')
def get_case_no_splash(id):
    print(f'{id}')
    return 'no splash cases'


print(app.url_map)

# 另一种注册机制：集中注册机制，2、装饰器注册
# 200项目很大，集中注册，URL没几个，小：@app.route()
# app.add_url_rule('/case',view_func=get_case)
# app.add_url_rule('/case',view_func=get_mouddle)


if __name__ == '__main__':
    app.run(debug=True)

# from : action entype:ww :保存图片 url:、upload：视图函数,<input name='file>
# url/函数：reder_template(显示表单)
# def upload():request.files['file'] a.save('path')
