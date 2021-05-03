# -*- coding: UTF-8 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get("/me/xx")
async def read_item_me():
    return {"me": 'me'}

@app.get("/me/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


@app.get("/")
async def main():
    return {"message": "Hello，FastAPI"}
    


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

