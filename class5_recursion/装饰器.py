"""
# ————————————————
# @Time    : 2021/2/8 15:51
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 装饰器.py
# ————————————————
"""


# 装饰器：开放封闭原则


def login (func):
    def fun ():
        userName = 'zgh'
        password = 'zhanggh'
        user = input("请输入账号：")
        pw = input("请输入密码：")
        if userName == user and pw == password:
            func()
        else:
            print("账号或者密码错误")

    return fun


@login  # @login:语法  ---》 index = login（index）
def index ():
    print("这是一个网站的首页")


# index.__closure__
# index()

# index = login(index)  # 这行代码功能与@login是一样的
# index()  # index --->fun  # print(index)
# 传进去的index在closure属性中

# 带参数的装饰器
# def add(func):
#     def fun(a,b):
#         print("相乘",a*b)
#         print("相除",a/b)
#         func(a,b)
#     return fun
#
# @add
# def add_num(a,b):
#     # 打印两个数相加
#     print("相加",a+b)
# add_num(11,22)

# 通用装饰器
def add (func):
    def fun (*args, **kwargs):
        print(args)
        print('装饰器的功能代码：登录')
        func(*args, **kwargs)

    return fun


@add
def index1 ():
    print("这是一个网站的首页")


@add
def goods_list (num):
    print("这是一个商品列表第{}页".format(num))


# index1()
# print('---------------')
# goods_list(9)


# 装饰器装饰类
def add (func):
    def fun (*args, **kwargs):
        print('装饰器的功能代码：登录')
        return func(*args, **kwargs)  # 装饰类要写return    装饰函数这里不一定要写return

    return fun


@add  # MyClass = add(MyClass)
class MyClass:
    def __init__ (self, name, age):
        self.name = name
        self.age = age


m = MyClass('luck','18')
print('m:', m)



'''
1、用类实现装饰器

2、多个装饰器装饰同一个函数

3、python中类里面三个装饰器函数

'''























