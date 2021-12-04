# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 21:55
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 05_flask_web表单.py
# @Software: PyCharm
from flask import Flask, render_template, Config
import time

# 初始化application
# static_url_path这个值必须以‘/’形式开头，前端访问的Hi好告诉用户，那个地址保存的静态文件
app = Flask(__name__, template_folder='html_file', static_url_path='/src', static_folder='src')

# 配置，.ini  .yml 配置 ，config.py Debug=True
# python数据类型：元组、字典、k:v  不可变字典 immutable_dict
# 类，不同的属性  setattr getattr
# setattr()
# Config
app.config['DEBUG'] = True
app.config['PORT'] = 5000

# 装饰器
"""
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
 
@decorator_name
def func():
    return("Function is running")
 
can_run = True
print(func())
# Output: Function is running
 
can_run = False
print(func())
# Output: Function will not run
"""


def log_time(f):
    def decorator(*args, **kwargs):
        print(f'{time.time()}')
        return f(*args, **kwargs)  # 装饰器返回必须是视图函数的返回值

    return decorator


# 可以统计流量

# 添加路由 view function
@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
@log_time  # 视图函数绑定，@app.route() ,其他装饰器函数必须放到app.route里面
def home(name=None):
    # num +=1  redis
    if name is None:
        name = 'world'
    print('hello')
    # return render_template('index.html')
    return 'hello %s' % name


print(__name__)
# 只有在模块内运行是进行，调用模块不运行该内容
if __name__ == '__main__':
    # 运行服务
    # debug 可以自动重启更新项目的文档变动更新
    app.run(host='127.0.0.1', port=app.config['PORT'], debug=app.config['DEBUG'])
