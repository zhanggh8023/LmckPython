# ————————————————
# @Time    : 2020/11/24 20:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : recursion递归函数.py
# ————————————————

# 递归函数


# 死循环
# def func ():
#     print('999999')
#     func() # pycharm 检测到无限递归会自动结束
# func()


'''递归边界'''
def fun(n):
    if n==1: # 递归的临界点是不再调用自身函数
        return 1
    else:
         return n*fun(n-1)

print(fun(4))

# 纯函数只依赖于他的参数，执行过程没有副作用，没有外部变量，就叫做纯函数







