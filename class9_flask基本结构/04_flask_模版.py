# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 20:33
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 04_flask_模版.py
# @Software: PyCharm

# app.run是测试，开发，调试使用，不要使用到生产环境（wsgi、nginx）
from flask import Flask, render_template

# 初始化application
# static_url_path这个值必须以‘/’形式开头，前端访问的Hi好告诉用户，那个地址保存的静态文件
app = Flask(__name__, template_folder='html_file', static_url_path='/src', static_folder='src')


# 添加路由 view function
@app.route('/')
def home():
    return render_template('index.html')


print(__name__)
# 只有在模块内运行是进行，调用模块不运行该内容
if __name__ == '__main__':
    # 运行服务
    # debug 可以自动重启更新项目的文档变动更新
    app.run(host='127.0.0.1', port='5000', debug=True)

    # MVC："../MVC.PNG"
    # 模型：model/sqlboy
    # 视图：view(返回的内容展示)/界面设计
    # 控制器：control(视图函数)/接受请求，公共业务、数据相关、响应结果
