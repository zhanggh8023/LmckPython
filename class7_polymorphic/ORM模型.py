"""
# ————————————————
# @Time    : 2021/2/10 20:23
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : ORM模型.py
# ————————————————
"""

"""
O(objects):类和对象

R（relation）：关系，关系数据库中的表格

M（mapping）：映射关系

"""
from django.db import models

models.CharField()


class CharFiled:
    def __init__ (self, max_lenght=20):
        self.max_lenght = max_lenght

    def __get__ (self, instance, owner):
        return self.value

    def __set__ (self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_lenght:
                self.value = value
            else:
                raise ValueError('字符串长度应该在{}长度以内'.format(self.max_lenght))
        else:
            raise TypeError('need a str')

    def __delete__ (self, instance):
        # del self.value
        self.value = None


class IntFiled:

    def __get__ (self, instance, owner):
        return self.value

    def __set__ (self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError('need a int')

    def __delete__ (self, instance):
        self.value = None


class UserModel(object):
    # 假设我这个是模型类
    name = CharFiled(max_lenght=20)  # 只能复制为字符串
    pwd = CharFiled(max_lenght=40)
    age = IntFiled()


m = UserModel()

m.name = "zgh"
m.pwd = "asdadgadlkfjasd;kfjad;sfasfadsfsdafff"
m.age = 18
print(m.name)
print(m.pwd)
print(m.age)
