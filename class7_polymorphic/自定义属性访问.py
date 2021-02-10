"""
# ————————————————
# @Time    : 2021/2/10 15:57
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 自定义属性访问.py
# ————————————————
"""

"""
object.__getattr__
当属性查找在通常的地方没有找到该属性时调用

object.__getattribute__
当找属性时，第一时间会调用该方法

object.__setattr__
设置属性时，调用该方法设置属性

object.__delattr__
在del obj.attr删除属性时触发

"""


class Test:

    def __init__ (self):
        self.age = 18

    # def __getattr__ (self, item):
    #     # 当我们方位属性的时候，如果属性不存在（出现AttrError），该方法会触发
    #     print('---------这是个getattr')
    #     # object.__getattribute__(self, item)
    #     return 100

    #
    # def __getattribute__(self, item):
    #     # 查找访问属性的时候，第一时间触发该方法去找属性
    #     print('这是个__getattribute')
    #     # return 999
    #     return super().__getattribute__(item)

    # def __setattr__(self, key, value):
    #     # 这个方法在给对象设置属性的时候触发
    #     if key == 'age':
    #         super().__setattr__(key,18)
    #     else:
    #         print('这个方法在给对象设置属性的时候触发')
    #         # print(key)
    #         # print(value)
    #         super().__setattr__(key, value)

    def __delattr__ (self, item):
        # 这个方法在删除属性的时候被触发
        if item == 'name':
            pass
        else:
            print('__delattr被调用')
            super().__delattr__(item)


t = Test()

t.name = 10
t.age = 999999

del t.name
del t.age

print(t.name)
print(t.age)  # print(t.name2)
