"""
# ————————————————
# @Time    : 2021/2/10 13:44
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __slots__限制对象属性.py
# ————————————————
"""


# 限制对象属性

class Base(object):
    # 指定类对象所能绑定的属性
    # 限制属性
    # 节约内存：定义了slots属性之后，那么该对象不会再自动生成__dict__属性
    __slots__ = ['name']
    pass

    def __init__ (self, name):
        self.name = name


b = Base('zgh')
# b,age = 18
b.name = "zgh"  # print(b.__dict__)  # 添加后没有dict属性
