# ————————————————
# @Time    : 2020/11/22 12:21
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 推导式comprehension.py
# ————————————————


# URL= ['page1','page2']

urls = []

for i in range(1, 10):
    url = 'page{}'.format(i)
    urls.append(url)

# print(urls)


# 列表推导式

urls1 = ['page{}'.format(i) for i in range(1, 100)]
# print(urls1)

# 字典推导式
dic1 = {i: i + 1 for i in range(10)}

# 推导式（）,使用ipython

tu = (i for i in range(10))  # 生成器对象
# print(tu)
#
# a=next(tu)
# print(a)
# print(next(tu))
'''
# 通过yield自定义生成器
def gen_fun():
    yield 100
    print('hello python!')

    yield 1000
    yield 100100

res = gen_fun()  # 返回生成器对象
print(next(res))  # 第一次取值
print(next(res))  # 第二次取值
print(next(res))  # 第三次取值
print(next(res))  # 最后报错
'''


# 生成器是迭代器的一种

# 列表
# 可迭代对象： 可以for循环便利的都是可迭代对象 内部 只实现了 __iter__方法
# li =[1,2,3,4]
#
# li1 = iter(li)  # iter()  __iter__
#
# # 迭代器 内部实现了__iter__之外，还实现了 __next__
# print(next(li1))    # __next__
# print(next(li1))
# print(type(li1))

# 生成器相比迭代器多了几种方法 send
# tu.send() # 发送  与生成器进行交互


def gen ():
    for i in range(1, 8):
        se = yield i
        print('se的值：', se)


g = gen()
print(next(g))

print(g.send(100))
print(next(g))
