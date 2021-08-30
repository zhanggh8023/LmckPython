# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 20:37
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 内存2.py
# @Software: PyCharm


class MyClass:
    pass


# 新式类 继承object
class Test(object):
    pass


t = Test()

print(type(t))

print(type(Test))

print(type(type))

# 字典遍历的时候不允许添加和修改元素
dic = {"a": 11, "b": 22}

data = list(dic.items())
dic["c"] = 33
print(data)

for k, v in data:
    print(k)
