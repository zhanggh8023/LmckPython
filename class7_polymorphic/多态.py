"""
# ————————————————
# @Time    : 2021/2/10 12:50
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 多态.py
# ————————————————
"""
'''
# 多态、封装、继承  三大面向对象编程特征
1、封装：将数据和方法放着一个类中构成封装

2、继承：一个类可以继承于一个类可以继承多个类，被继承的类叫父类（或者叫基类，baseclass）
继承的类叫子类

3、多态（polymorphism）：指的是一类事物有多种形态，一个抽象类有多个子类（因而多态的概念依赖于继承）
不同的子类对象调用相同的方法，产生不同的执行结果，多态可以增加diamante的灵活度

'''

"""
多态步骤：
1、定义一个父类（Base），实现某个方法（比如：run）
2、定义多个子类，在子类中重写父类的方法（run），每个子类run方法实现不同的功能
3、假设我们定义了一个函数，需要一个Base类型的对象的参数，那么调用函数函数的时候，
传入Base类不同的子类对象，那么这个函数就会执行不同的功能，这就是多态的体现。
"""


# 伪多态的实现

class Base(object):
    def run (self):
        print("-----base---run-----:路漫漫")


class Cat(Base):
    def run (self):
        print("--------cat----run---:会爬树")


class Dog(Base):
    def run (self):
        print("--------dog----run---:跑的快")


class Pig(Base):
    def run (self):
        print("--这是一个幂运算的操作")


# 鸭子类型的体现：静态语言来讲传入对象必须是Base类型或者他的子类，否则将无法调用run（）
# 动态语言上面传入的不一定是Base类型，也可以是其他类型，只要内部实现run（方法就行）

b_obj = Base()
c_obj = Cat()
d_obj = Dog()
p_obj = Pig()


# 子类的对象是输入父类的类型
# print(isinstance(c_obj,Cat))
# print(isinstance(c_obj,Base))


# python中函数的参数时没有类型限制的
# 假设func的参数需要Base类型的
def func (base_obj):
    base_obj.run()


func(b_obj)
func(c_obj)
func(d_obj)
func(p_obj)
"""
-----base---run-----:路漫漫
--------cat----run---:会爬树
--------dog----run---:跑的快
-----base---run-----:路漫漫
"""

# def func(a):
#     print(a)
#
# func(111)
# func("111222")
# func([1,2,3,4])
