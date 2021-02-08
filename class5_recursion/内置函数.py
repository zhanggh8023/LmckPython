"""
# ————————————————
# @Time    : 2021/2/8 10:51
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 内置函数.py
# ————————————————
"""
# 内置函数 ： python解释器内置很多函数，可直接调用，map、filter、zip等
# 过滤函数：第一参数：函数；第二个参数是可迭代对象
from collections.abc import Iterable
from functools import partial


def fun (n):
    # return True
    return n < 10


li = [1, 22, 122, 331, 11, 22, 33, 4, 5, 67]
res = filter(fun, li)
# li1 = []
# for i in li:
#     if i > 10 :
#         li1.append(i)
print(list(res))
#
# li2 = iter(li)
# li3 = (i for i in range(5))
#
# print(isinstance(li,Iterable))
# print(isinstance(li2,Iterable))
# print(isinstance(li3,Iterable))

# map函数
res2 = map(fun, li)
print(list(res2))

# zip函数
res3 = zip([1, 2, 3], [11, 22, 33])
print(list(res3))

dict1 = {'key': 1, 'name': 2, 'sex': 3}
print(list(dict1.items()))


# 匿名函数 ： 一种特殊函数，不需要使用def去事定义，也不用给函数起名字，用lamda表达式来定义，这种函数叫匿名函数
def func (a, b):
    c = a + b
    print(c)
    return a + b


# 运算符的优先级
# 匿名函数适用很简单的函数定义（只有一个表达式）
(lambda a, b: a + b)(1, 2)
# print(res((11, 22)))
res4 = filter(lambda x: x < 10, li)
print(list(res4))

li3 = [(lambda j: j % 5 == 0)(i) for i in range(10)]
print(li3)

a = 100
if a > 100:
    print(100)
else:
    print(22)
# 三目运算符
print(100) if a > 100 else print(22)


# 偏函数
li1 = [1,2,3,4,5,66,77,88,33]
li2 = [1,2,3,4,5,66,77,88,33]
li3 = [1,2,3,4,5,66,77,88,33]
li4 = [1,2,3,4,5,66,77,88,33]
li5 = [1,2,3,4,5,66,77,88,33]
li6 = [1,2,3,4,5,66,77,88,33]
li7 = [1,2,3,4,5,66,77,88,33]

#过滤小余5的数
filter(lambda x:x>5,li)

filter2=partial(filter,lambda x:x>5)

res =filter2(li)
print(list(res))
res2=filter2(li2)
print(list(li2))















