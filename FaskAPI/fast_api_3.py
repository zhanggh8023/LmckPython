"""
# -------------------------------
# @Time    : 2021/4/29 12:56
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : fast_api_3.py
# -------------------------------
"""

from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


#################################################
# 限制长度

@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    # None 代表默认值    ... 代表必填项
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}, {"item_id": "Baz"}]}
    if q:
        results.update({"q": q})
    return results
