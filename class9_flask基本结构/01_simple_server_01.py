# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 20:05
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: simple_server_01.py
# @Software: PyCharm


# 搭建服务、监听动作、处理程序、返回数据

from wsgiref.simple_server import make_server


def app(env, start_response):
    # env 获取请求相关数据
    # 状态码，header
    start_response('200 ok', [('content-type', 'text/plain')])
    return [b'hello']


server = make_server('', 9000, app)
server.serve_forever()
