# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 19:41
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 03_flask_abc.py
# @Software: PyCharm

# pip install flask
# werzung（application） jina2(渲染html）

# flask 组装大师  700 包含了大量的注释》》毛坯房
# ORM 另外装，数据库，三方插件
# django，flask》》》坑更多，爬坑，对web框架有更深入的理解认识


# flask >>用法，核心架构 》》simple_sever  response
# 用法和原理，实现细节和编程思维
# 从零开始的项目，测试工具，开发曲线平滑、中型大型

# import requests
# PEP8

from flask import Flask, request, render_template

# 初始化application
app = Flask(
    __name__,
    template_folder='html_file'
)


@app.route('/')
def index():
    # a=request
    args = request.args
    # 表单、file、json
    name = args.get('username')
    print(name)
    # return '<p style="color:red">hello</p>'
    return render_template('index.html')


# 运行服务
app.run()

# 为什么会404》》》》需要注册路由
# 为什么我的host，port没有定义，却有一个5000端口的服务？默认给到的
