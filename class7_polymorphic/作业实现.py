"""
# ————————————————
# @Time    : 2021/2/10 13:54
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 作业实现.py
# ————————————————
"""
import pymysql

"""
1、实现一个操作mysql的上下文管理器，可以自动断开
"""


class DB:
    # 数据库操作的上下文管理器
    def __init__ (self, data_conf):
        self.con = pymysql.connect(**data_conf)
        self.cursor = self.con.cursor()

    def __enter__ (self):
        return self.cursor

    def __exit__ (self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()


DATABASES_CONF = dict(host='localhost', user='root', password=123456, database='test', port=3306, charset='utf8')

with DB(DATABASES_CONF) as cur:
    cur.execute('select * from students;')
    print(cur.fetchall())

"""
2、描述__stots__属性的作用，并修改读取excel类中保存用例的类
限制对象属性，指定指定的slots的属性
节约内存
"""


# 报错用例的
class Case:
    __slots__ = ['case_id', 'title', 'url', 'data', 'excepted']

    def __init__ (self):
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.excepted = None


"""
3、面向对象的三大特征是什么、多态又是什么
特征：封装、继承、多态
多态：指的是一类事物有多种形态，一个抽象类有多个子类，
不同的子类对象调用相同的方法，产生不同的执行结果
"""

"""
4、私有属性怎么定义，不同的定义方式有什么区别
单下划线、双下划线开头
单下划线开头的，对外是公开的，可以直接访问
双下划线开头的，对外不能直接访问，为了保护这个变量（对外改了一个名字）

"""
