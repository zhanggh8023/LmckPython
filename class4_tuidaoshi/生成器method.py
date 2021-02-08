# ————————————————
# @Time    : 2020/11/24 20:33
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 生成器method.py
# ————————————————


# 生成器的三个方法 send  close throw

def gen ():
    for i in range(5):
        j = yield i
        print(j)


# send: 与生成器进行交互
g = gen()

print(next(g))
# print(g.send(100))  # 生成器需要在调用一次生成器后才可以传入

# print(next(g))


# close: 关闭生成器
# g.close()
# print(next(g))  # 无法调用


# throw:异常抛出,在生成器中内部主动引发一个异常
# #参数：异常类型   异常信息
# g.throw(ValueError, "hello python")
