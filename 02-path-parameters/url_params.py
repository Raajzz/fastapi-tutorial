# to run, uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{url_params}")
async def read_item(url_params: int):
  return {"items":url_params}