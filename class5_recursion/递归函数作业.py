"""
# ————————————————
# @Time    : 2021/2/8 12:03
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 递归函数作业.py
# ————————————————
"""

'''作业：
1、通过递归函数实现斐波那契数列，输入一个数列的位置数，返回斐波那契数列相应位置的值
斐波那契数列[1,1,2,3,5,8,13,21,34....],第一个数是1，后面的数等于前两个数相加的结果

2、古典问题：第三个月起每个月生一对兔子，小兔子长到第三个月后每个月又生一对兔子，加入兔子都不死，问每个月的兔子总数为多少
意味着生长期为2

3、小明有100元钱，打算买100本数，a类书籍5元一本，b类书籍3元一本，c类书籍1元两本，请用程序算出小明一共够多少中买法

'''


# 数列
def fixb (n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fixb(n - 1) + fixb(n - 2)


print(fixb(10))
# fixb(3) = fixb(2) + fixb(1)


# 兔子
'''
1
1
1+1（01）
2+1（02）
3+1（03）+1（0101）
5+1（04）+1（0102）+1（0201）
'''


def fun2 (n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fun2(n - 2) + fun2(n - 1))


print(fun2(6))

# 多少种方法
# 1、递归方式
import sys
# sys.setrecursionlimit(5000)   #可控制最大递归次数
count = 0
s=1
def count_book (a=0, b=0, c=0):
    '''计算买100本书籍的方式'''
    global s
    s +=1
    if a * 5 + b * 3 + c * 0.5 <= 100 and a + b + c == 100:  # 判断条件是否成立
        print(a, b, c)
        global count
        count += 1
    if a < int(100 / 5):
        if b < int(100 / 3):
            if c < (100):
                return count_book(a, b, c + 1)
            else:
                return count_book(a, b + 1)
        else:
            return count_book(a + 1)
try:
    count_book()
except:
    print(s)
# 递归次数最大限制是1000，python解释器默认的  这个方法次数20*33*100

money=100
book=100
count =0
for a in range(int(money/5)):
    for b in range(int(money/3)):
        for c in range(int(100)):
            if a * 5 + b * 3 + c * 0.5 <= 100 and a + b + c == 100:
                print(a,b,c)
                count +=1

print(count)






