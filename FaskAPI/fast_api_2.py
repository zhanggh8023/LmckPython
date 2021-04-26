"""
# -------------------------------
# @Time    : 2021/4/25 12:10
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : fast_api_2.py
# -------------------------------
"""

from fastapi import FastAPI
from enum import Enum

app = FastAPI()
fake_itmes_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_itmes_db[skip:skip + limit]


@app.get("/i/")
async def i(A: str = "HI..", B: str = "Hello..", C: str = "He.."):
    return {"cc": A + B + C}, {'dd': B + C}


@app.get("/ii/")
async def ii(A: int = 0, B: int = 10, C: int = 20):
    return {"cc": A + B + C}, {'dd': B + C}


@app.get("/iii/")
async def iii(A: int = 0, B: int = 10, C: int = 20):
    return 'A + B + C', A + B + C


# boot 与类型转换
@app.get("/xxx/{item_id}")
async def xxx(item_id: str, QQ: str = None, SS: bool = False):
    item = {"item_id": item_id}
    if QQ:
        item.update({"QQ": QQ})
    if not SS:  # 如果SS是假的
        item.update({"item_id": "This is SSSSSS"})
    return item


@app.get("/user/{user_id/item/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:  # 如果SS是假的
        item.update({"description": "This is an amazing item that has a long description"})
    return item


'''
class Name(str, Enum):
    Allan = '张三'
    Jon = '李四'
    Bob = '王五'


@app.get("/{who}")
async def get_day(who: Name):
    if who == Name.Allan:
        return {"who": who, "message": "张三是德国人🇩🇪"}
    if who.value == '李四':
        return {"who": who, "message": "李四是法国人🇫🇷"}
    return {"who": who, "message": "王五是英国人🇬🇧"}
'''

'''
# 前置可优先识别调用这个接口
@app.get("/me/xx")
async def read_item_me():
    return {"me": 'me'}


@app.get("/me/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}
'''


@app.get("/")
async def main():
    return {"message": "Hello FastAPI"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
