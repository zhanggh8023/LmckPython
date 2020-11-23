# @Time    : 2020/11/20 19:40
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : project集合元组.py
# @Software: PyCharm


'''
元组和列表的性能分析
 计算创建元组和列表所需的时间：ipython中使用timeit

计算时间模块介绍
'''
import timeit
from collections import namedtuple


def func ():
    for i in range(10):
        print(i)


'''
res = timeit.Timer(func).timeit(100)
print(res)

res2 = timeit.timeit('[1,2,3]')
print(res2)
'''

# 元组 命名元组
tu = ('musen', 18, 'nan')

# 创建命名元组,设定命名元组类型
student_info = namedtuple('student_info', ['name', 'age', 'gender'])

tu = student_info('musen', 18, 'nan')

print(tu.name)

print(type(tu))  # 元组类型名
print(type(student_info))  # 类
print(type(str))  # 类

# 字典和结合｛｝
li = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4]  # 利用集合对列表去重
li2 = list(set(li))
print(li2)

se = set()  # 空集合
set1 = {1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 2, 2, 2, 6, 6, 7}
print(set1)

dic = {}  # 空字典
print(type(dic))

# 集合添加元素 集合是可变的，是无序的
se.add('MuSen')
print(se)
se.update({111, 222, 333, 444})  # 等同于类别的extend
se.remove('MuSen')  # 删除
print(se)
se.clear()  # 清空
se.copy()  # 复制

# 3.7更新特性  字典存储开始根据添加顺序


'''
数值类型：1
序列类型：字符串、列表、元组
散列类型：字典、集合——特征是内部无序的


数据类型的可变和不可变：可hash，不可hash

'''
set2 = {1, 2, 3, 4, [1, 2, 3]}  # 字典、集合都是可以哈希的，放入列表等不可hash的会报错

print(set2)

'''

性能分析：
从时间上比较：集合 字典 元组 列表
占用内存比较：字典 集合 列表 元组
'''
