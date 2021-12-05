# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 15:48
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day02_views_视图函数的分离.py
# @Software: PyCharm
"""
1、路由相关：route() 路由：‘/’，flask 重定向308
2、注册机制：集中注册、装饰器注册
3、defaults={} 路由中默认参数
4、要注意 ：大型项目中的循环函数调用错误

什么是基于类的视图：可插拔视图

"""

import time

from flask import Flask
import views

app = Flask(__name__)
# 循环导入 大型项目的问题：
# 1、想用的时候导入；2、在合适的位置导入；3、导入文件具体方法代码，不是模块导入
from urls import *

time.sleep()
# cpython/GIL
# python 是任何领域的第二语言，万金油语言
# 可直接调用c语言
# io密集型，网络请求的


if __name__ == '__main__':
    app.run(debug=True)
