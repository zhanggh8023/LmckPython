# @Time    : 2020/11/20 19:40
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : project.py
# @Software: PyCharm


'''
元组和列表的性能分析
 计算创建元组和列表所需的时间：ipython中使用timeit

计算时间模块介绍
'''
import timeit


def func ():
    for i in range(10):
        print(i)


res = timeit.Timer(func).timeit(100)
print(res)

res2 = timeit.timeit('[1,2,3]')
print(res2)
