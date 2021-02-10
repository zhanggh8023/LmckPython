"""
# ————————————————
# @Time    : 2021/2/10 13:20
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 数据和自省.py
# ————————————————
"""


class Test:
    attr1 = 1000  # 公有属性
    # 私有属性
    _attr2 = 2000
    __attr3 = 3000


#
# c = Test()
#
# # 类属性可以通过类和实例对象去访问
#
# print(Test.attr1)
# print(c.attr1)
#
# # 单下划线先开头的私有属性
#
# print(Test._attr2)
# print(c._attr2)
#
# # 双下划线开通的私有属性
# # 双下划线开头的私有熟悉对外不能直接访问，微辣保护这个变量对外改了一个名字。
# # 在原有的属性名前面加了一个_方法名
# print(Test._Test__attr3)
# print(c._Test__attr3)
# print(Test.__dict__)


# 私有属性的继承问题
class A(Test):
    name = 'zhanggh'
    __name = "zgh"


a = A()

# print(a.attr1)
# print(a._attr2)
#
# # 可以继承
# print(a._Test__attr3)

print(Test.__dict__)
print(A.__dict__)  # 继承父类后，子类不会创建父类有的属性，可以节约内存
