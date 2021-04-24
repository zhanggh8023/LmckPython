"""
# -------------------------------
# @Time    : 2021/4/23 21:46
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : fastapi_main.py
# -------------------------------
"""
from typing import List
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# @app.get("/")
# async def main(request: Request):
#     return templates.TemplateResponse('index.html', {'request': request, 'hello': 'HI....'})

@app.get("/{item_id}/")
async def item_id(request: Request, item_id):
    return templates.TemplateResponse('/index.html', {'request': request, 'item_id': item_id})


@app.post("/user/")
async def create_unload_files(request: Request, test_1: str = Form(...), test_2: str = Form(...)):
    print("test_1:", test_1)
    print("test_2:", test_2)

    return templates.TemplateResponse('/index.html', {'request': request, 'test_1': test_1, 'test_2': test_2})


# @app.get("/")
# async def main(request: Request):
#     return templates.TemplateResponse('/post.html', {'request': request, 'hello': 'HI....'})


@app.post("/files/")
async def files(
        request: Request,
        files_list: List[bytes] = File(...),
        files_name: List[UploadFile] = File(...)):
    return templates.TemplateResponse("/index.html",
                                      {
                                          "request": request,
                                          "file_sizes": [len(file) for file in files_list],
                                          "filenames": [file.filename for file in files_name]
                                      })


@app.post("/create_file/")
async def create_file(
        request: Request,
        file: bytes = File(...),
        fileb: UploadFile = File(...),
        notes: str = Form(...)):
    return templates.TemplateResponse("/index.html",
                                      {
                                          "request": request,
                                          "file_size": len(file),
                                          "notes": notes,
                                          "fileb_content_type": fileb.content_type,
                                      })


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('/post.html', {'request': request, 'hello': 'HI....'})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
