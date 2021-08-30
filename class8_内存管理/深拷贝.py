# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 19:29
# @Email   : 849080458@qq.com
# @Author  : zgh
# @FileName: 深拷贝.py
# @Software: PyCharm

import copy

li = [1, 2, 3, 4]
list1 = [11, 22, li]

print(li, list1)

'''深浅拷贝 通冲只在列表嵌套列表的时候讨论'''
list2 = copy.deepcopy(list1)
list3 = list1.copy()
print(list2, list3)

li.remove(4)
print(li, list1)
print(list2)

'''循环引用，内存溢出'''

li1 = [1, 2]
li2 = [11, 22]
li1.append(li2[0])
li2.append(li1[0])
