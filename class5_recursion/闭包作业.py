"""
# ————————————————
# @Time    : 2021/2/8 20:09
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 闭包作业.py
# ————————————————
"""
import time

"""
1、一个完整的闭包必须满足那几个条件
#满足闭包条件：
#1、函数中嵌套函数
#2、外层函数返回内层嵌套函数名
#3、内层嵌套函数有引用外层的一个非全局变量


2、定义一个计算函数运行时间的装饰器（计算时间使用time模块实现）

3、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），邀请登录成功一次，
后续的函数都无需在输入用户名和密码

"""
# 计算运行时间
def wrapper(func):
    def count_time(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print("运行时间：{:.5f}".format(end_time-start_time))
    return count_time()



# 登录装饰器保持

with open('user.txt') as f:
    users = eval(f.read())

def login_check(func):
    """
    登录验证的装饰器
    :param func:
    :return:
    """
    def ado():
        if not users['token']: #判断token值是否为False
            print('============登录页面============')
            username = input("账号：")
            password = input("密码：")
            #登录校验
            if users['user'] == username and users['pwd']==password:
                users['token']= True  # 修改token值
                func()   # 调用被装饰的函数
        else:
            func()   # token值为True直接调用函数
    return ado


@login_check
def index():
    print("这是首页")

@login_check
def page1():
    print("这是第一页")

@login_check
def page2():
    print("这是第二页")



if __name__ == '__main__':
    index()
    page1()
    page2()









