"""
# ————————————————
# @Time    : 2021/2/8 20:39
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 装饰器使用.py
# ————————————————
"""

'''
1、用类实现装饰器

2、多个装饰器装饰同一个函数

3、python中类里面三个装饰器函数

'''

import time


# 计算运行时间
def wrapper (func):
    def count_time (*args, **kwargs):
        print('计算时间的装饰器')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("运行时间：{:.5f}".format(end_time - start_time))

    return count_time


# 登录装饰器保持

with open('../class5_recursion/user.txt') as f:
    users = eval(f.read())


def login_check (func):
    """
    登录验证的装饰器
    :param func:
    :return:
    """

    def ado (*args, **kwargs):
        print("登录校验装饰器")
        if not users['token']:  # 判断token值是否为False
            print('============登录页面============')
            username = input("账号：")
            password = input("密码：")
            # 登录校验
            if users['user'] == username and users['pwd'] == password:
                users['token'] = True  # 修改token值
                func(*args, **kwargs)  # 调用被装饰的函数
        else:
            func()  # token值为True直接调用函数

    return ado


@login_check  # count_time ==> func = login_check(func)  func===>ado
@wrapper  # func = wrapper(func)  func==>count_time
def func ():
    time.sleep(3)
    print('这是需要登录的时间装饰器函数')


# 从下往上装饰，从上往下执行
# func()


class MyTest(object):

    def __init__(self):
        # self.name=name
        pass

    @classmethod    # 被classmethod装饰之后，该方法就是一个类
    def add(cls):   #  cls:点的是类本身
        print("add")
        print('add中的cls：',cls)

    @staticmethod   # 静态方法 实例和类都可以调用
    def static():
        print("这是一个静态方法")

    @property   # 设定只读属性
    def read_attr(self):
        print("这个装饰器装饰器完了之后，该方法可以像属性一样被调用")
        return '18岁'

    def sub(self): # self代表的是实例本身
        print("sub")
        print('sub中的self：',self)

t= MyTest()
t.name='yuze'

print(t.name)
print(t.read_attr)

# t.add()
# t.sub()
# t.static()




















