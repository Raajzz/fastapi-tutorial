from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
  name: str
  description: Optional[str] = None 
  price: float 
  tax: Optional[float] = None
  
app = FastAPI()

@app.post("/items/{items_param}")
async def create_item(items_param: int, item: Item, q: Optional[str] = None):
  result = {"items_param":items_param, **(item.dict())}
  if q:
    result.update({"q":q})
  return result