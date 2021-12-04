# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 20:05
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 02_simple_server_02.py
# @Software: PyCharm

# 作业
from wsgiref.simple_server import make_server


class Router:
    def __init__(self):
        self.url = {}

    def route(self, path):
        def decorator(func):
            self.url[path] = func
            func()

        return decorator

    def __call__(self, env, start_response):
        path = env['PATH_INFO']

        if path in self.url:
            status = '200 ok'
            response_header = [('Content-Type', 'text/html')]
            start_response(status, response_header)
            return self.url[path]()
        else:
            status = '404 Not Found'
            response_header = [('Content-Type', 'text/html')]
            start_response(status, response_header)
            return [b'404 not found sources']


app = Router()


@app.route('/')
def index():
    yield b'this is the index'


@app.route('/login')
def login():
    yield 'this is the 大宝'.encode('gbk')


@app.route('/projects')
def projects():
    yield 'this is the 小宝'.encode('gbk')


#
# # 接口定义
# URL_PATTERNS = (
#     ('/', 'index'),
#     ('login/', 'login'),
#     ('projects/', 'projects')
# )
#
#
# class Dispatcher(object):
#     # 实现路由功能：
#     def _match(self, path):
#         path = path.split('/')[1]
#         print(path)
#         for url, app in URL_PATTERNS:
#             if path in url:
#                 return app
#
#     def __call__(self, environ, start_response):
#         # 拿到URL后面对的接口地址
#         path = environ.get('PATH_INFO','/')
#         # print(path,environ)
#         app = self._match(path)
#         if app:
#             print(app)
#             app = globals()[app]
#             return app(environ, start_response)
#         else:
#             start_response("404 NOT FOUND", [('Content-type', 'text/plain')])
#             return [b'page dose not exists']
#
#
# def index(environ, start_respose):
#     start_respose("200 ok", [('Content-type', 'text/html')])
#     print('首页')
#     return [b'index.html']
#
#
# def login(environ, start_respose):
#     start_respose("200 ok", [('Content-type', 'text/html')])
#     print('登录')
#     return [b'login.html']
#
#
# def projects(environ, start_respose):
#     start_respose("200 ok", [('Content-type', 'text/html')])
#     print('项目')
#     return [b'project.html']
#
#
# app = Dispatcher()


if __name__ == '__main__':
    server = make_server('', 9000, app)
    server.serve_forever()
