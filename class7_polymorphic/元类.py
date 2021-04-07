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

class MyMetaClass(type):
    """自定义的元类，将类的所有属性编程大写"""

    def __new__ (cls, name, bases, attr_dict, *args, **kwargs):
        print("最基础的自定义元类")  # 遍历属性名称
        for k, v in attr_dict.items():
            attr_dict.pop(k)
            attr_dict[k.upper()] = v

        # attr_dict['__slots__'] = ['name','age','gender']
        return super().__new__(cls, name, bases, attr_dict)


# 通过自定义的元类你来创建类
class Test(metaclass=MyMetaClass):
    name = 'zgh'
    age = 99
    gender = '男'


# 父类指定元类，子类可以继承所有指定的元类
class MyClass(Test):
    pass


t = Test()
