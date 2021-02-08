"""
# ————————————————
# @Time    : 2021/2/8 21:21
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : object-oriented面向对象魔术方法.py
# ————————————————
"""
#面向对象魔术方法:

class MyClass(object):

    def __init__(self,name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('这是一个new方法')
        # return super().__new__(cls)  #  调用父类方法
        return object.__new__(cls)   # 调用父类名字



m=MyClass('zgh')
print(m.name)
# print(m)


