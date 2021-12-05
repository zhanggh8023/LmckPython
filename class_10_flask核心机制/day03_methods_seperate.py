# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 20:12
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day03_methods_seperate.py
# @Software: PyCharm


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/uploads', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # 保存
        return 'url, success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
