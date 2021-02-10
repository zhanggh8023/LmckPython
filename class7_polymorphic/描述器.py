"""
# ————————————————
# @Time    : 2021/2/10 19:51
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 描述器.py
# ————————————————
"""


class Filed(object):
    # 一个类中，只要出现一下三个方法中的一个，那么该类就被称为描述器类
    def __get__ (self, instance, owner):
        print('访问属性的时候被触发')
        return self.value  # print(instance)  # print(owner)

    def __set__ (self, instance, value):
        print('------set__被触发')
        self.value = value  # print(self)  # print(instance)  # print(value)

    def __delete__ (self, instance):
        print('删除属性的时候会被触发')
        # del self.value
        self.value = None


class Model(object):
    name = 'zgh'
    attr = Filed()  # 描述器对象：会覆盖类属性相关操作


m = Model()
m.attr = 1000
del m.attr
# m.name = '被自己帅醒'
# print(m.name)
print(m.attr)
