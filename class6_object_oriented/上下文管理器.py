"""
# ————————————————
# @Time    : 2021/2/9 15:54
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 上下文管理器.py
# ————————————————
"""

# 上下文管理器

with open('test.txt', 'w+', encoding='utf8') as f:
    f.write('今天是周六，可以睡懒觉！')


# with 后面跟的是一个上下文管理器对象

class MyOpen(object):
    # 文件操作的上下文管理器类
    def __init__ (self, file_name, open_method, encoding='utf8'):
        self.file_name = file_name
        self.open_method = open_method
        self.encoding = encoding

    def __enter__ (self):
        self.f = open(self.file_name, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__ (self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_tb)
        print(exc_val)
        self.f.close()


with MyOpen('test.txt', 'r') as f:
    content = f.read()
    # print(name)
    print(content)
with MyOpen('test1.txt', 'w') as f:
    print(f)





















