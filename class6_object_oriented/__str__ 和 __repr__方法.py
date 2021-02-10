"""
# ————————————————
# @Time    : 2021/2/9 11:23
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __str__ 和 __repr__方法.py
# ————————————————
"""


# 使用print打印的时候触发的是__str__方法
# 交互环境直接输入变量的时候触发的是__repr__方法
# 注意点：
# 重写__str__和__repr__方法时，必须记得要写return
# return返回的必须是一个字符串对象

class MyClass(object):
    def __init__ (self, name):
        self.name = name

    def __str__ (self):
        print('__str__方法')
        return self.name

    def __repr__ (self):
        print('zhanggh')
        return '<MyClass.object-{}->'.format(self.name)

    def __call__ (self, *args, **kwargs):
        # 对象想函数一样被调用
        print("-----call----------")


m = MyClass('zgh')


# print(m)
# str(m)
# format(m)
#  当自身str方法没有时，会触发自身repr方法，都没有时，会去父类找
# res = repr(m)
# print(res)

# __call__方法
# 通过类来实现装饰器__call__

@MyClass
def fun ():
    print("-----------------")


# m()
fun()


class Test(object):
    def __call__ (self, *args, **kwargs):
        print('call方法调用')


t = Test()
# t()
