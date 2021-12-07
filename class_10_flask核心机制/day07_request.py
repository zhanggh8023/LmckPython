# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 22:14
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: day07_request.py
# @Software: PyCharm


from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    a = request
    # get 请求
    get_data = request.args
    # 表单
    form_data = request.form
    # json  header{applocation/json}
    json_data = request.json
    # file
    file_data = request.files

    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
