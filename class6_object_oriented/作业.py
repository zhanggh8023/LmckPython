"""
# ————————————————
# @Time    : 2021/2/9 15:23
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 作业.py
# ————————————————
"""

"""
第一题：通过装饰器实现单例模式，只要任意一类使用该装饰器，那么就会变成单例模式

"""


# 单例模式装饰器
def single (cls):
    instance = {}

    def fun (*args, **kwargs):
        if cls in instance:
            print('---已经存在了')
            return instance[cls]
        else:
            print('---不存在要添加一下')
            instance[cls] = cls(*args, **kwargs)
            return instance[cls]

    return fun


@single  # Test = single(Test)
class Test:
    print('---1')


t1 = Test()  # 第一次
t2 = Test()  # 第二次


@single
class Test2:
    print('---2')


t3 = Test2()


class Test3:
    print('---3')


"""
第二题：通过类实现一个通用的装饰器，既可以装饰函数，也可以装饰类，既可以装饰有参数的，
又可以装饰无参数的

"""
# 类实现装饰器
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('这个是装饰器里面的功能')
        self.func()
        print('装饰器---功能2')


@Decorator  # test1 = Decorator(test)
def test1():
    print("===原来的功能函数===")

test1()




"""
第三题：请描述 __new__ / __str__ / __repr__ / __call__分别在什么情况下会被触发

"""

# 见方法图片