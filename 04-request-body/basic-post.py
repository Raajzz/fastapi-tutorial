from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
  name: str
  description: Optional[str] = None 
  price: float 
  tax: Optional[float] = None

# This is kinda bad as there's no validation done 
class ItemWOTypes(BaseModel):
  name = ""
  description = ""
  price = 0.0
  tax = 0

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
  return item