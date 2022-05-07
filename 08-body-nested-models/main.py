from unittest import result
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None
  tags: list = []

result: dict = None

@app.post("/items/{item_id}")
async def update_items(item_id: int, item: Item):
  global result
  if(item_id == 0):
    result = {
      "item_0": item
    }
    return result
  else:
    result.update({
      'item_%s' % item_id :item
    })
    return result