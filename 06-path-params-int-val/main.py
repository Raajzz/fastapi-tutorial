from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id : Optional[str] = Path(None, min_length=5, max_length=15)):
  item_result = {"item_id":item_id}
  return item_result