# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 19:02
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : make_env.py
# @Software: PyCharm


"""
安装虚拟环境
pip install virtualenv

虚拟环境管理包
pip install virtualenvwrapper-win

创建目录.env或.virtualenv

配置环境变量
变量名称：WORKON_HOME
值：F:/.env

虚拟环境命令：
workon  列出所有虚拟环境
workon 【name】  进入指定虚拟环境
deactivate  退出当前虚拟环境
mkvirtualenv  -p python [name]  创建虚拟环境
rmvirtualenv  删除虚拟环境
"""

"""
pipenv的安装和使用
pip install pipenv


在工程目录下创建虚拟环境
pipenv install

查看当前环境下安装包
pipenv graph
"""