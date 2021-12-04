# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 20:05
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: simple_server_02.py
# @Software: PyCharm

# 作业
import json
from wsgiref.simple_server import make_server


def home(request):
    print('首页')
    return '首页{}'.format(request)


def login(request):
    print('登录')
    return '登录{}'.format(request)


def projects(request):
    print('项目')
    return '项目{}'.format(request)


# 路由
patterns = {
    '/': home,
    '/login': login,
    '/projects': projects,
}


def app(env, start_response):
    '''
    如果有很多的条件分支， 字典封装法
    :param env:
    :param start_response:
    :return:
    '''
    # application==>flask 核心对象
    # env 获取请求相关数据
    # 状态码，header
    url = env.get('PATH_INFO')
    params = env.get('QUERY_STRING')
    if url is None or (url not in patterns.keys()):
        # start_response('404 not found', [('content-type', 'text/html')])
        start_response('404 not found', [('content-type', 'application/json')])
        # return [b'<p style="color:red">page not found</p>']
        msg = json.dumps({'msg': 'page not found'})
        return [msg.encode()]
    start_response('200 ok', [('content-type', 'application/json')])
    resp = patterns.get(url)
    if resp is None:
        start_response('404 not found', [('content-type', 'application/json')])
        return [b'page not found']

    return [resp(params).encode()]

    # if url == '/':
    #     start_response('200 ok', [('content-type', 'application/json')])
    #     resp =home()
    #     return [resp.encode()]
    # elif url == '/login':
    #     start_response('200 ok', [('content-type', 'application/json')])
    #     resp = login()
    #     return [resp.encode()]
    # elif url == '/projects':
    #     start_response('200 ok', [('content-type', 'application/json')])
    #     resp = projects()
    #     return [resp.encode()]


# flask / django==>application
# flask run   django  run  ==> wsgi 协议===》调试

# uwsgi/gunicorn  /tornado/nginx==>使用这些
if __name__ == '__main__':
    server = make_server('', 9001, app)  # 回调 js
    server.serve_forever()
# wsgi python 协议
