"""
# ————————————————
# @Time    : 2021/2/9 9:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 单例模式.py
# ————————————————
"""
'''
# 单例模式：类每次实例化的时候都会创建新的对象，如果要求类只能被实例化一次怎么做呢
# 实现思路：
# 1、定义一个类属性，类记录该类是否创建过对象
# 2、在new方法中对类属性做判断：2.1没有创建就创建保存，并修改类属性值；2.2创建过就返回之前的
'''

# from class5_recursion.装饰器使用 import MyTest
# t1=MyTest()
# class MyClass(object):
#
#     def __init__(self,name):
#         self.name = name
#         print("__init__方法调用")
#
#     def __new__(cls, *args, **kwargs):
#         print('这是一个new方法')
#         # return super().__new__(cls)  #  调用父类方法
#         return object.__new__(cls)   # 调用父类名字
# m=MyClass('zgh')

# 单例模式

class MyTest(object):
    isstane = None  # 设置一个类属性用来记录这个类有没有创建过对象

    def __new__(cls, *args, **kwargs):
        if not cls.isstane:   # cls.isstane=None》False  not False 》true
            # 如果类属性__instance的值为None，那么就创建一个对象
            cls.isstane = object.__new__(cls)
            return cls.isstane
        else:
            return cls.isstane

# 装饰器实现单例模式


# t1 = MyTest()
# t1.name='zgh'
#
# t2=MyTest()
# print(t2.name)
# t3=MyTest()
#
# print(id(t1))
# print(id(t2))
# print(id(t3))

































