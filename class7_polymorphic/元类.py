"""
# ————————————————
# @Time    : 2021/2/10 21:06
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 元类.py
# ————————————————
"""


# 经典类 继承 instance类型（python2）
class MyClass:
    pass


# 新式类  继承object
class Test(object):
    pass


t = Test()

print(type(t))

print(type(Test))

print(type(type))

# type python3 中所有的类型都是同typy来创建出来的：元类

# object：python3中所有的类的顶级父类都是object
