# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 20:12
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day03_methods_seperate.py
# @Software: PyCharm
"""
什么是基于类的视图：可插拔视图》》》》来源django
视图有什么好处：
1、类可以继承
2、代码可以服用
3、可以定义多种类行为：方法、行为、属性：特征
4、类：不同的请求方法：get、post、upload、delete
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/uploads', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':  # 获取资源
        return render_template('index.html')
    if request.method == 'POST':  # 创建一个资源
        # 保存
        return 'url, success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
