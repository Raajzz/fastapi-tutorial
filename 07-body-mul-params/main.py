from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  description: Optional[str] = None 
  price: float
  tax: Optional[float] = None

class User(BaseModel):
  username: str
  full_name: str

@app.post("/items/{item_id}")
async def update_item(
  *,
  item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
  q: Optional[str] = None,
  item: Optional[Item] = None
):
  results = {"item_id":item_id}
  if q:
    results.update({"q":q})
  if item:
    results.update({"item":item})
  return results

# mutliple parameter while making a POST or a PUT request

@app.post("/multi_body/{item_id}")
async def update_item(
  *,
  item_id: int,
  q: str,
  item: Item,
  user: User
):
  results = {
    "item_id":item_id, 
    "q":q,
    "item":item,
    "user": user}
  return results
