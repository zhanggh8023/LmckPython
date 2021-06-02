# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 20:37
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 内存2.py
# @Software: PyCharm


class MyClass:
    pass


# 新式类 继承object
class Test(object):
    pass


t = Test()

print(type(t))

print(type(Test))

print(type(type))
