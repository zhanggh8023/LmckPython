"""
# ————————————————
# @Time    : 2021/2/8 15:31
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 闭包.py
# ————————————————
"""


def login ():
    print("登录")

# 闭包
def func (num,b):
    print("----func被调用-----")
    # num =100
    def count_book ():
        print(b)
        print(num)
        print("这是计算书买房时的函数")

    return count_book

# func()() # 可调用内部函数
res = func(1999,'python')
# print(res.__closure__)


#满足闭包条件：
#1、函数中嵌套函数
#2、外层函数返回内层嵌套函数名
#3、内层嵌套函数有引用外层的一个非全局变量

# 作用；实现数据的锁定 提高稳定性





















