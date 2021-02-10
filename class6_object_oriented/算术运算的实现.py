"""
# ————————————————
# @Time    : 2021/2/9 16:10
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 算术运算的实现.py
# ————————————————
"""


class MyStr(object):
    def __init__ (self, data):
        self.data = data

    def __str__ (self):
        return self.data

    def __add__ (self, other):
        print('----触发了add方法----')
        print(self)
        print(other)
        return self.data + other.data

    def __sub__ (self, other):
        return self.data.replace(other.data, '')


s1 = MyStr("zgh")
s2 = MyStr('666')
print(s1)
print(s2)
print(s1 + s2)

s3 = MyStr(s1 + s2)
print(s3 - s2)
