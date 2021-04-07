"""
# ————————————————
# @Time    : 2021/4/7 19:56
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 垃圾回收机制.py
# ————————————————
"""

li1 = [1, 2]
li2 = [11, 22]
li1.append(li2[0])
li2.append(li1[0])

print(li1, li2)

# GC模块

import gc

res = gc.get_threshold()

print(res)
